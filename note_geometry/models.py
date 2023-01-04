from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student_note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note_sub = models.CharField(max_length=50, null=True, blank=True)
    note_title = models.CharField(max_length=50)
    note_para = models.TextField(max_length=500)