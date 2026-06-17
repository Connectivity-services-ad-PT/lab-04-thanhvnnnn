import re
import logging
from typing import Optional
from datetime import datetime

logger = logging.getLogger(__name__)

def mask_sensitive_data(text: str, pattern: str = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}') -> str:
    """Mask email addresses in logs"""
    return re.sub(pattern, '[MASKED_EMAIL]', text)

def format_log_message(notification_id: str, recipient: str, type: str) -> str:
    """Format log message with masking"""
    if type == 'email':
        masked = mask_sensitive_data(recipient)
    elif type == 'sms':
        # Keep last 4 digits only
        masked = '****' + recipient[-4:] if len(recipient) >= 4 else '****'
    else:
        masked = recipient[:10] + '...' if len(recipient) > 10 else recipient
    
    return f"Notification {notification_id} sent to {masked} via {type}"

def validate_json_schema(data: dict, required_fields: list) -> Optional[str]:
    """Validate required fields in JSON data"""
    missing = [field for field in required_fields if field not in data]
    if missing:
        return f"Missing required fields: {', '.join(missing)}"
    return None

def generate_notification_id() -> str:
    """Generate unique notification ID with timestamp prefix"""
    from uuid import uuid4
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    short_uuid = str(uuid4())[:8]
    return f"notify_{timestamp}_{short_uuid}"