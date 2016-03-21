from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Jobs(models.Model):
	''' Descripcion  de los empleos '''
	title = models.CharField(max_length=100, unique=True)
	company = models.CharField(max_length=50)
	companyDescription = models.TextField()
	jobDescription = models.TextField()
	skills = models.TextField()
	postedDate = models.DateField(auto_now_add=True)
	salaryRange = models.CharField(max_length=30)
	slug = models.SlugField(max_length=50, unique=True)
	jobImage = models.ImageField(upload_to='company/%Y/%m/%d')
	category = models.ManyToManyField("Category", blank=True)

class Category(models.Model):
	''' Un empleo puede tener muchas categorias '''
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name