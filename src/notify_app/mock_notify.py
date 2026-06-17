import uuid
import json
import logging
from datetime import datetime
from typing import Dict, Any
from .models import NotificationRequest
from .config import config

logger = logging.getLogger(__name__)

class MockNotificationService:
    """Mock notification service - no real notifications sent"""
    
    def __init__(self):
        self.sent_notifications = []
        self.total_sent = 0
        self.failures = 0
        
    def send(self, request: NotificationRequest) -> Dict[str, Any]:
        """
        Mock sending a notification
        Returns a simulated delivery result
        """
        notification_id = str(uuid.uuid4())
        
        # Log the mock sending
        log_entry = {
            "id": notification_id,
            "type": request.type,
            "recipient": request.recipient,
            "subject": request.subject,
            "message_preview": request.message[:100] + ("..." if len(request.message) > 100 else ""),
            "timestamp": request.timestamp.isoformat(),
            "received_at": datetime.now().isoformat(),
            "mock_mode": config.MOCK_MODE
        }
        
        # Store in memory
        self.sent_notifications.append(log_entry)
        self.total_sent += 1
        
        # Simulate processing delay (1-50ms)
        import time
        time.sleep(0.01)  # 10ms delay
        
        # Simulate occasional failure (5% of the time for testing)
        import random
        if random.random() < 0.05 and config.MOCK_MODE:
            self.failures += 1
            logger.warning(f"Simulated failure for notification {notification_id}")
            raise Exception("Simulated notification failure")
        
        # Log to console for visibility
        print("\n" + "="*60)
        print(f"[MOCK NOTIFICATION] ID: {notification_id}")
        print(f"Type: {request.type.upper()}")
        print(f"Recipient: {request.recipient}")
        if request.subject:
            print(f"Subject: {request.subject}")
        print(f"Message: {request.message}")
        print(f"Timestamp: {request.timestamp}")
        print("="*60 + "\n")
        
        logger.info(f"Mock notification sent: {notification_id} to {request.recipient}")
        
        return {
            "id": notification_id,
            "status": "accepted",
            "mock_mode": config.MOCK_MODE,
            "sent_at": datetime.now().isoformat(),
            "provider": f"mock-{request.type}"
        }
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get mock service statistics"""
        return {
            "total_sent": self.total_sent,
            "failures": self.failures,
            "success_rate": ((self.total_sent - self.failures) / max(self.total_sent, 1)) * 100,
            "mock_mode": config.MOCK_MODE,
            "recent_notifications": self.sent_notifications[-10:]  # Last 10 notifications
        }
    
    def clear_history(self):
        """Clear notification history"""
        self.sent_notifications = []
        self.total_sent = 0
        self.failures = 0
        logger.info("Mock notification history cleared")

# Singleton instance
mock_service = MockNotificationService()

def send_mock_notification(request: NotificationRequest) -> Dict[str, Any]:
    """Helper function to send mock notification"""
    return mock_service.send(request)

def get_mock_stats() -> Dict[str, Any]:
    """Get mock service statistics"""
    return mock_service.get_statistics()