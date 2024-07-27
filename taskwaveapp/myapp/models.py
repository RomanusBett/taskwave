from django.db import models
from django.utils import timezone

class Job(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]
    
    
    job_Id = models.AutoField(primary_key=True)
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    retry_count = models.IntegerField(default=0)
    max_retries = models.IntegerField(default=3)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(default=0)
    concurrency_limit = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'Job {self.job_Id} - {self.recipient}'
    
    def can_retry(self):
        return self.retry_count < self.max_retries
    
    def is_shcheduled(self):
        return self.created_at and self.scheduled_at > timezone.now()
    
    def schedule(self, run_at):
        self.schedule = run_at
        self.save()
        
    def mark_as_completed(self):
        self.status = 'completed'
        self.save()
        
    def mark_as_failed(self):
        self.status = 'failed'
        self.save()
        
    