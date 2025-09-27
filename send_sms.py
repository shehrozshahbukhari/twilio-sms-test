# Twilio SMS Test Script
# Author: Syed Shehroz Bukhari
# Purpose: Personal project to test Twilio SMS API for sending/receiving messages

from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "your_auth_token"

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Example: Send an SMS
message = client.messages.create(
    body="Hello, this is a test message from my personal Twilio project!",
    from_="+1xxxxxxxxxx",   # Your Twilio number
    to="+92xxxxxxxxxx"     # Your personal number
)

print("Message SID:", message.sid)
