from django.contrib import admin

# Register your models here.
from .models import Profile,Task

admin.site.register(Profile)
admin.site.register(Task)