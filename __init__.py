"""
Lukrum FX Models API Client Package

This package provides a complete API client for the Lukrum FX Models API,
including DTO classes and a comprehensive client for all endpoints.
"""

from .api_client import LukrumModelsAPIClient
from lukrum_lib.dto.models_api_dto import (
    Model,
    Observation,
    Property,
    PropertyType,
    TradeHistory,
    ModelStats,
    ActiveStats,
    TradeHistoryResponse,
    ModelCreateRequest,
    ModelUpdateRequest,
    ObservationCreateRequest,
    ObservationUpdateRequest,
    PropertyCreateRequest,
    PropertyUpdateRequest,
)
from lukrum_lib.shared_api.exceptions import (
    LukrumAPIError as LukrumFXAPIException,
    LukrumAPIError as APIRequestException,
    AuthenticationError as AuthenticationException,
    ValidationError as ValidationException,
    NotFoundError as NotFoundException,
    RateLimitError as RateLimitException,
)

__all__ = [
    'LukrumModelsAPIClient',
    'Model',
    'Observation',
    'Property',
    'PropertyType',
    'TradeHistory',
    'ModelStats',
    'ActiveStats',
    'TradeHistoryResponse',
    'ModelCreateRequest',
    'ModelUpdateRequest',
    'ObservationCreateRequest',
    'ObservationUpdateRequest',
    'PropertyCreateRequest',
    'PropertyUpdateRequest',
    'LukrumFXAPIException',
    'APIRequestException',
    'AuthenticationException',
    'ValidationException',
    'NotFoundException',
    'RateLimitException'
]
