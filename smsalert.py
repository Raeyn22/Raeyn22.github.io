# backend/services/sms.py
from africastalking.Service import SMSService

def send_sms_alert(phone_number: str, message: str):
    # Initialize Africa's Talking SMS service
    sms = SMSService(username="your_username", api_key="your_api_key")
    
    try:
        # Send SMS
        response = sms.send(message, [phone_number])
        return response
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return None
