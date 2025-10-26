# Lukrum FX Models API Client

A comprehensive Python client for the Lukrum FX Models API. This client provides easy-to-use methods for interacting with all API endpoints including models, observations, properties, and trade history.

## Features

- **Complete API Coverage**: All endpoints from the Lukrum FX Models API specification
- **Type Safety**: Full type hints and DTO classes for all data structures
- **Error Handling**: Comprehensive exception handling with specific error types
- **Context Manager Support**: Use with `with` statements for automatic resource cleanup
- **Request/Response Validation**: Built-in validation for API requests and responses

## Installation

Install requirements, then import from `lukrum_models_client` and use DTOs from `lukrum_lib`:

```bash
pip install requests
```

## Quick Start

```python
from lukrum_models_client import LukrumModelsAPIClient
from lukrum_lib.dto.models_api_dto import ModelCreateRequest

# Initialize the client
client = LukrumModelsAPIClient(
    base_url="http://162.19.66.207:5001",
    api_key="your-api-key-here"
)

# Get all models
models = client.get_models()
print(f"Found {len(models)} models")

# Create a new model
new_model = ModelCreateRequest(
    name="My Trading Model",
    model_uuid="unique-model-id",
    active=1,
    exit_type="TP",
    tp_pips=50,
    sl_pips=25
)

result = client.create_model(new_model)
print(f"Model created: {result}")

# Always close the client
client.close()
```

## Using Context Manager

```python
from lukrum_models_client import LukrumModelsAPIClient

with LukrumModelsAPIClient(api_key="your-api-key") as client:
    models = client.get_models(active=1)
    print(f"Active models: {len(models)}")
    # Client automatically closed
```

## API Endpoints

### Models

- `get_models()` - Get all models with optional filtering
- `create_model()` - Create a new model
- `get_model_by_uuid()` - Get model by UUID
- `update_model()` - Update an existing model
- `delete_model()` - Delete a model
- `get_active_stats()` - Get active model statistics
- `get_entry_granularities()` - Get available entry granularities
- `get_exit_granularities()` - Get available exit granularities

### Observations

- `get_observations()` - Get observations with optional model filtering
- `create_observation()` - Create a new observation
- `get_observation()` - Get observation by ID
- `update_observation()` - Update an observation
- `delete_observation()` - Delete an observation

### Properties

- `get_properties()` - Get properties with optional model filtering
- `create_property()` - Create a new property
- `get_property()` - Get property by ID
- `update_property()` - Update a property
- `delete_property()` - Delete a property

### Property Types

- `get_property_types()` - Get all property types
- `get_property_type()` - Get property type by ID

### Trade History

- `get_trade_history()` - Get trade history with comprehensive filtering
- `get_model_stats()` - Get aggregated statistics for a model

## Data Transfer Objects (DTOs)

The client includes comprehensive DTO classes for all API entities:

### Core Entities
- `Model` - Trading model representation
- `Observation` - Model observation data
- `Property` - Model property data
- `PropertyType` - Property type definition
- `TradeHistory` - Trade history entry

### Request DTOs
- `ModelCreateRequest` - For creating models
- `ModelUpdateRequest` - For updating models
- `ObservationCreateRequest` - For creating observations
- `ObservationUpdateRequest` - For updating observations
- `PropertyCreateRequest` - For creating properties
- `PropertyUpdateRequest` - For updating properties

### Response DTOs
- `ModelStats` - Model statistics
- `ActiveStats` - Active model statistics
- `TradeHistoryResponse` - Trade history response with pagination

## Error Handling

The client provides specific exception types for different error scenarios:

```python
from lukrum_models_client import (
    APIRequestException,
    AuthenticationException,
    ValidationException,
    NotFoundException,
    RateLimitException
)

try:
    models = client.get_models()
except AuthenticationException:
    print("Invalid API key")
except ValidationException as e:
    print(f"Validation error: {e}")
    print(f"Details: {e.validation_errors}")
except NotFoundException:
    print("Resource not found")
except RateLimitException:
    print("Rate limit exceeded")
except APIRequestException as e:
    print(f"API error: {e}")
```

## Advanced Usage

### Filtering Models

```python
# Get active models for specific instrument
active_models = client.get_models(
    active=1,
    entry_granularity="5M,15M",
    exit_granularity="15M"
)

# Get models by UUIDs
specific_models = client.get_models(uuids="uuid1,uuid2,uuid3")
```

### Trade History Filtering

```python
# Get recent trades with filters
recent_trades = client.get_trade_history(
    model_id=123,
    trade_type="LONG",
    trade_result="TP",
    ts_open_start="2024-01-01T00:00:00Z",
    limit=50,
    order_by="ts_open",
    order="desc"
)
```

### Model Statistics

```python
# Get comprehensive model statistics
stats = client.get_model_stats(model_id=123)
print(f"Win rate: {stats.win_rate:.2%}")
print(f"Total pips: {stats.total_pips}")
print(f"Average pips: {stats.average_pips}")
```

## Configuration

The client supports configuration through the constructor:

```python
client = LukrumModelsAPIClient(
    base_url="http://162.19.66.207:5001",  # API base URL
    api_key="your-api-key"                 # Authentication key
)
```

## Examples

See `example_usage.py` for comprehensive examples of using the API client.

## API Specification

This client is built against the Lukrum FX Models API specification available at:
http://162.19.66.207:5001/apispec.json

## Requirements

- Python 3.7+
- requests library

## License

Part of the Lukrum FX data processing project.
