# python file for OTP genrate!

import random
import string
from twilio.rest import Client
from django.conf import settings

def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

def send_otp(phone_number, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Welcome to Rewards App. Your One-Time Password (OTP) is: {otp}.Enter this code to verify your account and begin earning rewards with our easy tasks.",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=f"+91{phone_number}",
    )
    return message.sid