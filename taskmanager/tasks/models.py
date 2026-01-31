from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title= models.CharField(default='Untitled',max_length=150)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    
    def __str__(self):
        return self.title