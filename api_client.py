"""
Lukrum FX Models API Client

A comprehensive client for interacting with the Lukrum FX Models API.
Provides methods for all endpoints including models, observations, properties, and trade history.
"""

from typing import Optional, List, Dict, Any

from lukrum_lib.shared_api.base_client import BaseAPIClient
from .config import ModelsAPIConfig
from lukrum_lib.dto.models_api_dto import (
    Model, Observation, Property, PropertyType, TradeHistory,
    ModelStats, ActiveStats, TradeHistoryResponse,
    ModelCreateRequest, ModelUpdateRequest,
    ObservationCreateRequest, ObservationUpdateRequest,
    PropertyCreateRequest, PropertyUpdateRequest,
)
from lukrum_lib.shared_api.exceptions import (
    LukrumAPIError as APIRequestException,
    AuthenticationError as AuthenticationException,
    ValidationError as ValidationException,
    NotFoundError as NotFoundException,
    RateLimitError as RateLimitException,
)


class LukrumModelsAPIClient(BaseAPIClient):
    """
    Client for the Lukrum FX Models API.
    
    This client provides methods to interact with all Models API endpoints including:
    - Models management
    - Observations
    - Properties
    - Property Types
    - Trade History
    """
    
    def __init__(self, config: Optional[ModelsAPIConfig] = None):
        """
        Initialize the API client.
        
        Args:
            config: Configuration object. If None, will load from environment variables.
        """
        self.config = config or ModelsAPIConfig.from_env()
        super().__init__(self.config)
    
    def get_version(self) -> str:
        """Get the API version."""
        return "1.0.0"
    
    # Models endpoints
    
    def get_models(self, 
                   uuids: Optional[str] = None,
                   active: Optional[int] = None,
                   entry_granularity: Optional[str] = None,
                   exit_granularity: Optional[str] = None) -> List[Model]:
        """
        Get all models or filter by parameters.
        
        Args:
            uuids: Comma-separated list of model UUIDs to filter
            active: Filter by active status (1 or 0)
            entry_granularity: Comma-separated list of entry granularities to filter
            exit_granularity: Comma-separated list of exit granularities to filter
            
        Returns:
            List of Model objects
        """
        params = {}
        if uuids is not None:
            params['uuids'] = uuids
        if active is not None:
            params['active'] = active
        if entry_granularity is not None:
            params['entry_granularity'] = entry_granularity
        if exit_granularity is not None:
            params['exit_granularity'] = exit_granularity
        
        response = self._make_request('GET', '/models', params=params)
        models_data = response.get('models', [])
        
        return [Model(**model_data) for model_data in models_data]
    
    def create_model(self, model_request: ModelCreateRequest) -> Dict[str, Any]:
        """
        Create a new model.
        
        Args:
            model_request: Model creation request data
            
        Returns:
            Response data
        """
        return self._make_request('POST', '/models', data=model_request.to_dict())
    
    def get_model_by_uuid(self, uuid: str) -> Model:
        """
        Get a specific model by UUID.
        
        Args:
            uuid: Model UUID
            
        Returns:
            Model object
        """
        response = self._make_request('GET', f'/models/{uuid}')
        return Model(**response)
    
    def update_model(self, model_id: int, update_request: ModelUpdateRequest) -> Dict[str, Any]:
        """
        Update a model by ID.
        
        Args:
            model_id: Model ID
            update_request: Model update request data
            
        Returns:
            Response data
        """
        return self._make_request('PUT', f'/models/{model_id}', data=update_request.to_dict())
    
    def delete_model(self, model_id: int) -> Dict[str, Any]:
        """
        Delete a model by ID.
        
        Args:
            model_id: Model ID
            
        Returns:
            Response data
        """
        return self._make_request('DELETE', f'/models/{model_id}')
    
    def get_active_stats(self) -> ActiveStats:
        """
        Get counts of active models by instrument and entry/exit granularity.
        
        Returns:
            ActiveStats object
        """
        response = self._make_request('GET', '/models/active_stats')
        return ActiveStats(**response)
    
    def get_entry_granularities(self) -> List[str]:
        """
        Get distinct entry granularities.
        
        Returns:
            List of entry granularities
        """
        response = self._make_request('GET', '/models/entry_granularities')
        return response.get('entry_granularities', [])
    
    def get_exit_granularities(self) -> List[str]:
        """
        Get distinct exit granularities.
        
        Returns:
            List of exit granularities
        """
        response = self._make_request('GET', '/models/exit_granularities')
        return response.get('exit_granularities', [])
    
    # Observations endpoints
    
    def get_observations(self, model_id: Optional[int] = None) -> List[Observation]:
        """
        Get all observations or filter by model ID.
        
        Args:
            model_id: Filter by model ID
            
        Returns:
            List of Observation objects
        """
        params = {}
        if model_id is not None:
            params['model_id'] = model_id
        
        response = self._make_request('GET', '/observations', params=params)
        observations_data = response.get('observations', [])
        
        return [Observation(**obs_data) for obs_data in observations_data]
    
    def create_observation(self, observation_request: ObservationCreateRequest) -> Dict[str, Any]:
        """
        Create a new observation.
        
        Args:
            observation_request: Observation creation request data
            
        Returns:
            Response data
        """
        return self._make_request('POST', '/observations', data=observation_request.to_dict())
    
    def get_observation(self, observation_id: int) -> Observation:
        """
        Get a specific observation by ID.
        
        Args:
            observation_id: Observation ID
            
        Returns:
            Observation object
        """
        response = self._make_request('GET', f'/observations/{observation_id}')
        return Observation(**response)
    
    def update_observation(self, observation_id: int, update_request: ObservationUpdateRequest) -> Dict[str, Any]:
        """
        Update an observation.
        
        Args:
            observation_id: Observation ID
            update_request: Observation update request data
            
        Returns:
            Response data
        """
        return self._make_request('PUT', f'/observations/{observation_id}', data=update_request.to_dict())
    
    def delete_observation(self, observation_id: int) -> Dict[str, Any]:
        """
        Delete an observation.
        
        Args:
            observation_id: Observation ID
            
        Returns:
            Response data
        """
        return self._make_request('DELETE', f'/observations/{observation_id}')
    
    # Properties endpoints
    
    def get_properties(self, model_id: Optional[int] = None) -> List[Property]:
        """
        Get all properties or filter by model ID.
        
        Args:
            model_id: Filter by model ID
            
        Returns:
            List of Property objects
        """
        params = {}
        if model_id is not None:
            params['model_id'] = model_id
        
        response = self._make_request('GET', '/properties', params=params)
        properties_data = response.get('properties', [])
        
        return [Property(**prop_data) for prop_data in properties_data]
    
    def create_property(self, property_request: PropertyCreateRequest) -> Dict[str, Any]:
        """
        Create a new property.
        
        Args:
            property_request: Property creation request data
            
        Returns:
            Response data
        """
        return self._make_request('POST', '/properties', data=property_request.to_dict())
    
    def get_property(self, property_id: int) -> Property:
        """
        Get a specific property by ID.
        
        Args:
            property_id: Property ID
            
        Returns:
            Property object
        """
        response = self._make_request('GET', f'/properties/{property_id}')
        return Property(**response)
    
    def update_property(self, property_id: int, update_request: PropertyUpdateRequest) -> Dict[str, Any]:
        """
        Update a property.
        
        Args:
            property_id: Property ID
            update_request: Property update request data
            
        Returns:
            Response data
        """
        return self._make_request('PUT', f'/properties/{property_id}', data=update_request.to_dict())
    
    def delete_property(self, property_id: int) -> Dict[str, Any]:
        """
        Delete a property.
        
        Args:
            property_id: Property ID
            
        Returns:
            Response data
        """
        return self._make_request('DELETE', f'/properties/{property_id}')
    
    # Property Types endpoints
    
    def get_property_types(self) -> List[PropertyType]:
        """
        Get all property types.
        
        Returns:
            List of PropertyType objects
        """
        response = self._make_request('GET', '/property_types')
        property_types_data = response.get('property_types', [])
        
        return [PropertyType(**pt_data) for pt_data in property_types_data]
    
    def get_property_type(self, property_type_id: int) -> PropertyType:
        """
        Get a specific property type by ID.
        
        Args:
            property_type_id: Property type ID
            
        Returns:
            PropertyType object
        """
        response = self._make_request('GET', f'/property_types/{property_type_id}')
        return PropertyType(**response)
    
    # Trade History endpoints
    
    def get_trade_history(self,
                         model_id: Optional[int] = None,
                         model_uuid: Optional[str] = None,
                         trade_type: Optional[str] = None,
                         trade_result: Optional[str] = None,
                         ts_open_start: Optional[str] = None,
                         ts_open_end: Optional[str] = None,
                         ts_close_start: Optional[str] = None,
                         ts_close_end: Optional[str] = None,
                         min_pips: Optional[str] = None,
                         max_pips: Optional[str] = None,
                         min_balance: Optional[str] = None,
                         max_balance: Optional[str] = None,
                         open: Optional[str] = None,
                         limit: Optional[int] = None,
                         offset: Optional[int] = None,
                         order_by: Optional[str] = None,
                         order: Optional[str] = None) -> TradeHistoryResponse:
        """
        Get trade history with comprehensive filtering.
        
        Args:
            model_id: Filter by model ID
            model_uuid: Filter by model UUID
            trade_type: Filter by trade type (LONG/SHORT)
            trade_result: Filter by trade result (TP/SL)
            ts_open_start: Filter trades opened after this timestamp
            ts_open_end: Filter trades opened before this timestamp
            ts_close_start: Filter trades closed after this timestamp
            ts_close_end: Filter trades closed before this timestamp
            min_pips: Minimum pips
            max_pips: Maximum pips
            min_balance: Minimum balance
            max_balance: Maximum balance
            open: Filter for open trades (true/false)
            limit: Limit number of results
            offset: Offset for pagination
            order_by: Field to order by (default ts_open)
            order: Order direction (asc/desc)
            
        Returns:
            TradeHistoryResponse object
        """
        params = {}
        if model_id is not None:
            params['model_id'] = model_id
        if model_uuid is not None:
            params['model_uuid'] = model_uuid
        if trade_type is not None:
            params['trade_type'] = trade_type
        if trade_result is not None:
            params['trade_result'] = trade_result
        if ts_open_start is not None:
            params['ts_open_start'] = ts_open_start
        if ts_open_end is not None:
            params['ts_open_end'] = ts_open_end
        if ts_close_start is not None:
            params['ts_close_start'] = ts_close_start
        if ts_close_end is not None:
            params['ts_close_end'] = ts_close_end
        if min_pips is not None:
            params['min_pips'] = min_pips
        if max_pips is not None:
            params['max_pips'] = max_pips
        if min_balance is not None:
            params['min_balance'] = min_balance
        if max_balance is not None:
            params['max_balance'] = max_balance
        if open is not None:
            params['open'] = open
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        if order_by is not None:
            params['order_by'] = order_by
        if order is not None:
            params['order'] = order
        
        response = self._make_request('GET', '/trade-history', params=params)
        
        trades_data = response.get('trades', [])
        trades = [TradeHistory(**trade_data) for trade_data in trades_data]
        
        return TradeHistoryResponse(
            count=response.get('count', 0),
            trades=trades
        )
    
    def get_model_stats(self, model_id: int) -> ModelStats:
        """
        Get aggregated statistics for a model's trade history.
        
        Args:
            model_id: Model ID
            
        Returns:
            ModelStats object
        """
        response = self._make_request('GET', f'/trade-history/stats/{model_id}')
        return ModelStats(**response)
    
