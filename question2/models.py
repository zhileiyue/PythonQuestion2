from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Result(models.Model):
	num = models.IntegerField(blank=True, null=True)
	res = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return (u"%s") % ('fabc result')