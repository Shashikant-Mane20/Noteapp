from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteList(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateField()
    desc=models.TextField(max_length=500)
    is_active=models.BooleanField(default=1)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")