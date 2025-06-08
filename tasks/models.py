from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    
    def __str__(self):
        return f"{self.title} (Due: {self.due_date})"
    
    class Meta:
        ordering = ['due_date', 'priority'] 