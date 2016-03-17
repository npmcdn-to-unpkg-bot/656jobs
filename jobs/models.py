from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Jobs(models.Model):
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=50)
	companyDescription = models.TextField()
	jobDescription = models.TextField()
	postedDate = models.DateField(auto_now_add=True)
	salaryRange = models.CharField(max_length=10)
	jobImage = models.ImageField(upload_to='company/%Y/%m/%d')