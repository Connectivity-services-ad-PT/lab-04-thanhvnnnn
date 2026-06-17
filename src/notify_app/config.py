import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # Server config
    APP_NAME = os.getenv("APP_NAME", "Notify Service")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Mock mode (no real notifications)
    MOCK_MODE = os.getenv("NOTIFY_MOCK_MODE", "true").lower() == "true"
    
    # Rate limiting (optional for production)
    RATE_LIMIT_PER_MINUTE = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
    
    # Supported notification types
    SUPPORTED_TYPES = ["email", "sms", "webhook", "inapp"]
    
    # Max message length
    MAX_MESSAGE_LENGTH = int(os.getenv("MAX_MESSAGE_LENGTH", "1000"))
    
    # Logging format
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Health check config
    HEALTH_CHECK_ENABLED = True
    HEALTH_CHECK_PATH = "/health"

config = Config()