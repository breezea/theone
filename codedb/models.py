from django.db import models
from django.utils import timezone

import pytz
from datetime import datetime
tz = pytz.timezone('Asia/Shanghai')

# Create your models here.

class CodeModel(models.Model):
    title = models.CharField(max_length = 100, )
    author = models.CharField(max_length=20,) 
    languages = models.CharField(max_length=20)
    desc = models.CharField(max_length=500)
    tags = models.CharField(max_length=100)
    code = models.CharField(max_length=10000)

    insertTime = models.DateTimeField(auto_now=True)
    
    # def save(self, *args, **kwargs):
    #     self.insertTime = datetime.now().astimezone(tz)
    #     print(datetime.now(), self.insertTime)
    #     self.title = 'hello world'
    #     super().save(*args, **kwargs)
    