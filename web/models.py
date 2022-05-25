from fileinput import filename
from os import P_NOWAIT
from pickle import FALSE, TRUE
from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from django.contrib.auth.models import User


# Create your models here.
class  Website(models.Model):
    title=models.CharField(max_length=100,unique=True)
    summary=models.TextField()
    created_on=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_generated=models.BooleanField(default=False)

class Page(models.Model):
    text = models.TextField(verbose_name='Page Content (MARKDOWN only)',)
    filename=models.CharField(verbose_name="filename",max_length=60,unique=TRUE)
    website=models.ForeignKey(Website,on_delete=models.CASCADE)
