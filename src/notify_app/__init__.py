import uuid
from datetime import datetime

def send_mock_notification(req):
    # Simulate async sending
    print(f"[MOCK] Sending {req.type} to {req.recipient}: {req.message}")
    return {
        "id": str(uuid.uuid4()),
        "sent_at": datetime.now().isoformat()
    }