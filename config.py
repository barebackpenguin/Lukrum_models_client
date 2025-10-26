"""
Configuration management for the Lukrum Models API client.
"""

import os
from typing import Optional
from dataclasses import dataclass

from lukrum_lib.shared_api.config import BaseAPIConfig


@dataclass
class ModelsAPIConfig(BaseAPIConfig):
    """Configuration class for the Lukrum Models API client."""
    
    base_url: str = "http://162.19.66.207:5001"
    api_key: Optional[str] = None
    timeout: int = 30
    max_retries: int = 3
    verify_ssl: bool = False  # Set to False for self-signed certificates
    
    def __post_init__(self):
        """Load configuration from environment variables if not provided."""
        # Load API key from environment if not provided
        if not self.api_key:
            self.api_key = os.getenv('LUKRUM_MODELS_API_KEY')
        
        # Override with environment variables if they exist
        if os.getenv('LUKRUM_MODELS_BASE_URL'):
            self.base_url = os.getenv('LUKRUM_MODELS_BASE_URL')
        
        if os.getenv('LUKRUM_MODELS_TIMEOUT'):
            self.timeout = int(os.getenv('LUKRUM_MODELS_TIMEOUT'))
        
        if os.getenv('LUKRUM_MODELS_MAX_RETRIES'):
            self.max_retries = int(os.getenv('LUKRUM_MODELS_MAX_RETRIES'))
        
        if os.getenv('LUKRUM_MODELS_VERIFY_SSL'):
            self.verify_ssl = os.getenv('LUKRUM_MODELS_VERIFY_SSL').lower() == 'true'
        
        # Call parent __post_init__ for common setup
        super().__post_init__()
    
    def validate(self) -> None:
        """Validate the configuration."""
        if not self.api_key:
            raise ValueError("API key is required. Set LUKRUM_MODELS_API_KEY environment variable or pass api_key parameter.")
        
        # Call parent validation for common checks
        super().validate()
    
    @classmethod
    def from_env(cls) -> 'ModelsAPIConfig':
        """Create configuration from environment variables."""
        return cls()
    
    @classmethod
    def from_dict(cls, config_dict: dict) -> 'ModelsAPIConfig':
        """Create configuration from dictionary."""
        return cls(**config_dict)
