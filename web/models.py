from fileinput import filename
from os import P_NOWAIT
from pickle import FALSE, TRUE
from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from django.contrib.auth.models import User


# Create your models here.
class  Website(models.Model):
    title=models.CharField(max_length=100,unique=TRUE)
    summary=models.TextField()
    created_on=models.DateTimeField(auto_now=TRUE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_generated=models.BooleanField(default=FALSE)

class Page(models.Model):
    text = MarkdownField(rendered_field='text_rendered',use_editor=True, use_admin_editor=True, validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()
    filename=models.CharField(max_length=60,unique=TRUE)
    website=models.ForeignKey(Website,on_delete=models.CASCADE)
