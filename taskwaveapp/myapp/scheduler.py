from .emails import scheduledSend
from .models import Job  
import datetime


def emailcron():
    scheduledEmails = Job.objects.all()
    
    for mail in scheduledEmails:
        if mail.scheduled_at >= datetime.now():
            print('email should be sent')
            
        else: 
            print('email should not be sent')
            
    