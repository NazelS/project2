from django.db import models

from django.db import models
from test1.models import Comment

class Post(models.Model):
    post=models.CharField(max_length=50, unique=True)
    comment=models.ForeignKey(
        Comment,on_delete=models.CASCADE)
