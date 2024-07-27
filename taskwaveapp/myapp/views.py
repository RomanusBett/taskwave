from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
import json


@api_view(['POST'])
def postJob(request):
    try: 
        data = json.loads(request.body)
        recipient  = data.get('recipient')
        subject = data.get('subject')
        body = data.get('body')
        max_retries = data.get('max_retries', 3)
        scheduled_at = data.get('scheduled_at')
        priority = data.get('priority', 0)
        
        if not recipient or not subject or not body:
            return JsonResponse({'error': 'recipient, body and subject fields are required'})

        
        job = Job(
            recipient = recipient,
            subject = subject,
            body = body,
            max_retries = max_retries,
            scheduled_at = scheduled_at,
            priority = priority
        )
        Job.save()
        
        return JsonResponse({'message': 'email schedule created success', 'job_id': job.id}, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid '}, status = 400)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 500)
