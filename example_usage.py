"""
Example usage of the Lukrum FX API client.

This file demonstrates how to use the API client for various operations.
"""

from api_client import LukrumModelsAPIClient
from lukrum_lib.dto.models_api_dto import (
    ModelCreateRequest, ObservationCreateRequest, 
    PropertyCreateRequest, ModelUpdateRequest,
)
from lukrum_models_client import (
    APIRequestException, AuthenticationException, 
    ValidationException, NotFoundException,
)


def main():
    """Example usage of the Lukrum FX API client."""
    
    # Initialize the client
    client = LukrumModelsAPIClient(
        base_url="http://162.19.66.207:5001",
        api_key="your-api-key-here"  # Replace with actual API key
    )
    
    try:
        # Example 1: Get all models
        print("=== Getting all models ===")
        models = client.get_models()
        print(f"Found {len(models)} models")
        for model in models[:3]:  # Show first 3 models
            print(f"Model: {model.name} (UUID: {model.model_uuid})")
        
        # Example 2: Get active models only
        print("\n=== Getting active models ===")
        active_models = client.get_models(active=1)
        print(f"Found {len(active_models)} active models")
        
        # Example 3: Create a new model
        print("\n=== Creating a new model ===")
        new_model_request = ModelCreateRequest(
            name="Test Model",
            model_uuid="test-model-uuid-123",
            active=1,
            exit_type="TP",
            tp_pips=50,
            sl_pips=25,
            instrument="EURUSD",
            entry_granularity="5M",
            exit_granularity="15M"
        )
        
        try:
            create_result = client.create_model(new_model_request)
            print(f"Model created successfully: {create_result}")
        except ValidationException as e:
            print(f"Validation error: {e}")
            if e.validation_errors:
                print(f"Validation details: {e.validation_errors}")
        
        # Example 4: Get model statistics
        print("\n=== Getting model statistics ===")
        if models:
            first_model = models[0]
            if first_model.id:
                try:
                    stats = client.get_model_stats(first_model.id)
                    print(f"Model {first_model.name} stats:")
                    print(f"  Total trades: {stats.total_trades}")
                    print(f"  Win rate: {stats.win_rate:.2%}")
                    print(f"  Average pips: {stats.average_pips:.2f}")
                except NotFoundException:
                    print(f"Model {first_model.id} not found")
        
        # Example 5: Get trade history with filters
        print("\n=== Getting trade history ===")
        trade_history = client.get_trade_history(
            limit=10,
            order_by="ts_open",
            order="desc"
        )
        print(f"Found {trade_history.count} trades (showing {len(trade_history.trades)})")
        
        for trade in trade_history.trades[:3]:  # Show first 3 trades
            print(f"Trade: {trade.trade_type} - {trade.trade_result} - {trade.pips} pips")
        
        # Example 6: Get property types
        print("\n=== Getting property types ===")
        property_types = client.get_property_types()
        print(f"Found {len(property_types)} property types")
        for pt in property_types[:3]:  # Show first 3 property types
            print(f"Property Type: {pt.name} (ID: {pt.id})")
        
        # Example 7: Create an observation
        print("\n=== Creating an observation ===")
        if models:
            first_model = models[0]
            if first_model.id:
                observation_request = ObservationCreateRequest(
                    model_id=first_model.id,
                    value={"signal": "BUY", "confidence": 0.85}
                )
                
                try:
                    obs_result = client.create_observation(observation_request)
                    print(f"Observation created: {obs_result}")
                except ValidationException as e:
                    print(f"Observation validation error: {e}")
        
        # Example 8: Get active statistics
        print("\n=== Getting active statistics ===")
        active_stats = client.get_active_stats()
        print("Active models by entry granularity:")
        for entry_stat in active_stats.by_entry[:3]:
            print(f"  {entry_stat['granularity']}: {entry_stat['count']} models")
        
        print("Active models by exit granularity:")
        for exit_stat in active_stats.by_exit[:3]:
            print(f"  {exit_stat['granularity']}: {exit_stat['count']} models")
        
    except AuthenticationException as e:
        print(f"Authentication error: {e}")
    except APIRequestException as e:
        print(f"API request error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    finally:
        # Always close the client
        client.close()


def example_with_context_manager():
    """Example using the client as a context manager."""
    
    with LukrumModelsAPIClient(
        base_url="http://162.19.66.207:5001",
        api_key="your-api-key-here"
    ) as client:
        
        try:
            # Get models
            models = client.get_models(active=1)
            print(f"Active models: {len(models)}")
            
            # Get granularities
            entry_granularities = client.get_entry_granularities()
            exit_granularities = client.get_exit_granularities()
            
            print(f"Entry granularities: {entry_granularities}")
            print(f"Exit granularities: {exit_granularities}")
            
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Lukrum FX API Client Example ===")
    main()
    
    print("\n=== Context Manager Example ===")
    example_with_context_manager()
