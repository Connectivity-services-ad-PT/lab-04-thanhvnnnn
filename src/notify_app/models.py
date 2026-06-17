from pydantic import BaseModel, Field, validator, field_validator
from typing import Optional
from datetime import datetime
import re

class NotificationRequest(BaseModel):
    """Request model for sending notification"""
    
    type: str = Field(..., description="Type of notification: email, sms, webhook, inapp")
    recipient: str = Field(..., description="Recipient address (email, phone number, URL, or user_id)")
    subject: Optional[str] = Field(None, max_length=200, description="Subject line (for email)")
    message: str = Field(..., min_length=1, max_length=1000, description="Notification content")
    timestamp: datetime = Field(..., description="ISO 8601 timestamp")
    metadata: Optional[dict] = Field(None, description="Additional metadata")
    
    @field_validator('type')
    @classmethod
    def validate_type(cls, v):
        allowed = ["email", "sms", "webhook", "inapp"]
        if v not in allowed:
            raise ValueError(f'type must be one of: {", ".join(allowed)}')
        return v
    
    @field_validator('recipient')
    @classmethod
    def validate_recipient(cls, v, info):
        notification_type = info.data.get('type')
        
        if notification_type == 'email':
            # Basic email validation
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, v):
                raise ValueError('Invalid email format')
        
        elif notification_type == 'sms':
            # Phone number validation (basic)
            phone_pattern = r'^\+?[0-9]{10,15}$'
            if not re.match(phone_pattern, v):
                raise ValueError('Invalid phone number format. Use E.164 format: +84123456789')
        
        elif notification_type == 'webhook':
            # URL validation
            url_pattern = r'^https?://[^\s/$.?#].[^\s]*$'
            if not re.match(url_pattern, v):
                raise ValueError('Invalid webhook URL')
        
        elif notification_type == 'inapp':
            # User ID validation (alphanumeric + underscore)
            user_pattern = r'^[a-zA-Z0-9_]{3,50}$'
            if not re.match(user_pattern, v):
                raise ValueError('Invalid user ID format')
        
        return v
    
    @field_validator('subject')
    @classmethod
    def validate_subject(cls, v, info):
        if info.data.get('type') == 'email' and not v:
            raise ValueError('Subject is required for email notifications')
        return v
    
    @field_validator('timestamp')
    @classmethod
    def validate_timestamp(cls, v):
        # Ensure timestamp is not in the future (allow 5 sec tolerance)
        from datetime import timezone
        now = datetime.now(timezone.utc)
        if v > now:
            # Allow 5 seconds tolerance for clock sync issues
            if (v - now).total_seconds() > 5:
                raise ValueError('Timestamp cannot be more than 5 seconds in the future')
        return v

class NotificationResponse(BaseModel):
    """Response model for successful notification"""
    
    success: bool = Field(True, description="Operation success status")
    notification_id: str = Field(..., description="Unique notification ID")
    message: str = Field(..., description="Response message")
    timestamp: datetime = Field(..., description="Server timestamp")
    queued: bool = Field(False, description="Whether notification was queued")
    estimated_delivery_seconds: Optional[int] = Field(None, description="Estimated delivery time")

class ProblemDetails(BaseModel):
    """RFC 7807 Problem Details for API errors"""
    
    type: str = Field("/errors/notification-failed", description="Error type URI")
    title: str = Field(..., description="Short error title")
    status: int = Field(..., description="HTTP status code", ge=400, lt=600)
    detail: str = Field(..., description="Detailed error explanation")
    instance: str = Field(..., description="Request path")
    timestamp: Optional[datetime] = Field(None, description="Error timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "type": "/errors/invalid-request",
                "title": "Validation Error",
                "status": 400,
                "detail": "Invalid recipient format for email",
                "instance": "/notifications",
                "timestamp": "2026-05-13T08:30:00+07:00"
            }
        }