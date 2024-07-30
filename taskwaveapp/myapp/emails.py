from django.core.mail import EmailMessage
from rest_framework.decorators import api_view
from dotenv import load_dotenv
import os

load_dotenv()

def scheduledSend():
    try:
        email = EmailMessage('subject', 'Body', to=['bettromanus@gmail.com'])
        email.send()
    
    except Exception as e:
        print(e)

scheduledSend()