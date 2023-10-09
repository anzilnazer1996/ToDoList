from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseClass(models.Model):
    uuid = models.SlugField(default=uuid.uuid4, unique=True)
    active_status = models.BooleanField(default=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Profile(AbstractUser):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='user-images')
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
    def __str__(self):
        return f'{self.name}'

class Task(BaseClass):
    priority_choices = [('Low','Low'),
                        ('Medium','Medium'),
                        ('High','High')
                        ]
    user = models.ForeignKey('Profile',on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100) 
    task_description = models.TextField()
    task_priority = models.CharField(max_length=100,choices=priority_choices)
    task_due_date = models.DateField()
    task_completed =models.BooleanField(default=False)    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task'
    def __str__(self):
        return f'{self.user.name} {self.task_name} {self.task_priority}'