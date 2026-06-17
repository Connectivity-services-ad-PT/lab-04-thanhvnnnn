from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
import os
import logging
import uuid
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=getattr(logging, os.getenv("LOG_LEVEL", "INFO")),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Notify Service - Smart Campus",
    description="Notification service for Smart Campus Operations Platform",
    version="1.0.0"
)

# ==================== MODELS ====================

class NotificationRequest(BaseModel):
    """Request model for sending notification"""
    
    type: str = Field(..., description="Type: email, sms, webhook, inapp")
    recipient: str = Field(..., description="Recipient address")
    subject: Optional[str] = Field(None, description="Subject for email")
    message: str = Field(..., description="Notification content")
    timestamp: datetime = Field(..., description="ISO 8601 timestamp")
    
    @validator('type')
    def validate_type(cls, v):
        allowed = ["email", "sms", "webhook", "inapp"]
        if v not in allowed:
            raise ValueError(f'type must be one of: {", ".join(allowed)}')
        return v
    
    @validator('recipient')
    def validate_recipient(cls, v, values):
        notification_type = values.get('type')
        
        if notification_type == 'email':
            if '@' not in v or '.' not in v:
                raise ValueError('Invalid email format')
        elif notification_type == 'sms':
            # Basic phone validation
            if not v.replace('+', '').replace('-', '').isdigit():
                raise ValueError('Invalid phone number')
        elif notification_type == 'webhook':
            if not v.startswith(('http://', 'https://')):
                raise ValueError('Webhook must start with http:// or https://')
        
        return v
    
    @validator('subject')
    def validate_subject(cls, v, values):
        if values.get('type') == 'email' and not v:
            raise ValueError('Subject is required for email')
        return v

class NotificationResponse(BaseModel):
    success: bool
    notification_id: str
    message: str
    timestamp: datetime

class ProblemDetails(BaseModel):
    type: str
    title: str
    status: int
    detail: str
    instance: str

# ==================== MOCK SERVICE ====================

def send_mock_notification(request: NotificationRequest):
    """Mock sending notification - no real delivery"""
    notification_id = str(uuid.uuid4())
    
    # Log to console
    print("\n" + "="*60)
    print(f"[MOCK] Sending {request.type} notification")
    print(f"To: {request.recipient}")
    if request.subject:
        print(f"Subject: {request.subject}")
    print(f"Message: {request.message}")
    print(f"Timestamp: {request.timestamp}")
    print(f"Notification ID: {notification_id}")
    print("="*60 + "\n")
    
    logger.info(f"Mock notification sent: {notification_id} to {request.recipient}")
    
    return {
        "id": notification_id,
        "status": "accepted",
        "sent_at": datetime.now().isoformat()
    }

# ==================== ENDPOINTS ====================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "notify-service",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/notifications", status_code=202)
async def send_notification(request: NotificationRequest):
    """Send a notification through specified channel"""
    try:
        logger.info(f"Received notification request: type={request.type}, recipient={request.recipient}")
        
        # Send mock notification
        result = send_mock_notification(request)
        
        return NotificationResponse(
            success=True,
            notification_id=result["id"],
            message=f"Notification accepted for delivery via {request.type}",
            timestamp=datetime.now()
        )
        
    except Exception as e:
        logger.error(f"Failed to send notification: {str(e)}")
        
        problem = ProblemDetails(
            type="/errors/notification-failed",
            title="Notification Failed",
            status=500,
            detail=str(e),
            instance="/notifications"
        )
        
        raise HTTPException(
            status_code=500,
            detail=problem.dict()
        )

# ==================== ERROR HANDLERS ====================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions with ProblemDetails format"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "type": "/errors/http-error",
            "title": "HTTP Error",
            "status": exc.status_code,
            "detail": str(exc.detail),
            "instance": request.url.path
        }
    )

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    """Handle validation errors"""
    return JSONResponse(
        status_code=400,
        content={
            "type": "/errors/validation-error",
            "title": "Validation Error",
            "status": 400,
            "detail": str(exc),
            "instance": request.url.path
        }
    )

# ==================== RUN SERVER ====================

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )