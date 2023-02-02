from django.db import models



class Comment(models.Model):
    commend=models.CharField(max_length=50)
