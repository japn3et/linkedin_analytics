from .data_generator import LinkedInPost, LinkedInProfileGenerator
from .kafka_simulator import KafkaQueueSimulator
from .crawler import LinkedInCrawler
from .database import DatabaseHandler

__version__ = "0.1.0"


__all__ = [
    "LinkedInPost",
    "LinkedInProfileGenerator",
    "KafkaQueueSimulator",
    "LinkedInCrawler",
    "DatabaseHandler",
]


__author__ = "Japneet"
__email__ = "japneet2943@gmail.com"
__description__ = "A LinkedIn post simulator and analyzer"

# Configuration defaults
DEFAULT_CONFIG = {
    "TARGET_POSTS": 500,
    "NUM_WORKERS": 2,
    "DB_PATH": "linkedin_posts.db",
    "SIMULATION_SETTINGS": {
        "min_posts_per_profile": 1,
        "max_posts_per_profile": 5,
        "image_probability": 0.3,
        "video_probability": 0.2,
        "min_content_words": 20,
        "max_content_words": 200,
    }
}

def get_version():
    """Return the package version."""
    return __version__

def get_default_config():
    """Return a copy of the default configuration."""
    return DEFAULT_CONFIG.copy()

def initialize_simulator(config=None):
    """
    Initialize all components of the LinkedIn simulator.
    
    Args:
        config (dict, optional): Configuration dictionary to override defaults
        
    Returns:
        tuple: (LinkedInCrawler, DatabaseHandler) initialized instances
    """
    if config is None:
        config = get_default_config()
    
    kafka_queue = KafkaQueueSimulator()
    profile_generator = LinkedInProfileGenerator()
    crawler = LinkedInCrawler(kafka_queue, profile_generator)
    db_handler = DatabaseHandler(config.get('DB_PATH', DEFAULT_CONFIG['DB_PATH']))
    return crawler, db_handler

class LinkedInSimulatorError(Exception):
    """Base exception class for LinkedIn Simulator."""
    pass

class ConfigurationError(LinkedInSimulatorError):
    """Raised when there's an error in configuration."""
    pass

class SimulationError(LinkedInSimulatorError):
    """Raised when there's an error during simulation."""
    pass

class DatabaseError(LinkedInSimulatorError):
    """Raised when there's an error with database operations."""
    pass

def validate_config(config):
    """
    Validate configuration dictionary.
    
    Args:
        config (dict): Configuration to validate
        
    Raises:
        ConfigurationError: If configuration is invalid
    """
    required_keys = ['TARGET_POSTS', 'NUM_WORKERS', 'DB_PATH']
    for key in required_keys:
        if key not in config:
            raise ConfigurationError(f"Missing required configuration key: {key}")
    
    if config['NUM_WORKERS'] < 1:
        raise ConfigurationError("NUM_WORKERS must be at least 1")
    
    if config['TARGET_POSTS'] < 1:
        raise ConfigurationError("TARGET_POSTS must be at least 1")

def setup_logging():
    """
    Configure logging for the package.
    """
    import logging
    
    logger = logging.getLogger('linkedin_simulator')
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger


logger = setup_logging()

def version_info():
    """
    Return a dictionary containing version information.
    
    Returns:
        dict: Version information including dependencies
    """
    import sys
    import platform
    
    return {
        "linkedin_simulator": __version__,
        "python": sys.version,
        "platform": platform.platform(),
        "machine": platform.machine()
    }