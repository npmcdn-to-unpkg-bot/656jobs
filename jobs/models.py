from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Company(models.Model):
	''' Descipcion de la Empresa '''
	company = models.CharField(max_length=50)
	companyDescription = models.TextField()
	companyWebsite = models.CharField(max_length=50, unique=True, blank=True, null=True)
	companyEmail = models.EmailField(max_length=75)
	companyImage = models.ImageField(upload_to='company/%Y/%m/%d')
	
	def  __unicode__(self):
		return self.company

class Jobs(models.Model):
	''' Descripcion  de los empleos '''
	company = models.ForeignKey(Company)
	title = models.CharField(max_length=100)
	jobDescription = models.TextField()
	skills = models.TextField()
	postedDate = models.DateField(auto_now_add=True)
	SALARY = (
		('1', 'Menos de 10,000'),
		('2', '10,000 - 20,000'),
		('3', '20,000 - 30,000'),
		('4', '30,000 - 40,000'),
		('5', '40,000 - 60,000'),
		('6', '60,000 - 80,000'),
		('7', '80,000 o superior')
	)

	TIPO_DE_EMPLEO = (
		('C','Tiempo Completo'),
		('T','Temporal')
	)

	salaryRange = models.CharField(max_length=1,choices=SALARY)
	jobtype = models.CharField(max_length=1,choices=TIPO_DE_EMPLEO)
	slug = models.SlugField(max_length=50, unique=True)
	category = models.ManyToManyField("Category", blank=True)

	def salary_verbose(self):
		return dict(Jobs.SALARY)[self.salaryRange]

	def jobtype_verbose(self):
		return dict(Jobs.TIPO_DE_EMPLEO)[self.jobtype]
		
class Category(models.Model):
	''' Un empleo puede tener muchas categorias '''
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User)
	professional_name = models.CharField(max_length=100)
	profile_image = models.ImageField(upload_to='profile_images/%Y/%m/%d')
	resume = models.FileField(upload_to='resumes/%Y/%m/%d', help_text='PDF')
	summary = models.TextField(blank=True,null=True)
	contact = models.TextField(blank=True,null=True, help_text='Agrega todas las formas en que podamos contactarte')

	def __unicode__(self):
		return self.user.username
		
class WorkExperience(models.Model):
	user = models.ForeignKey(User)
	place = models.CharField(max_length=100)
	start_date = models.DateField() 
	end_date = models.DateField()
	work_description = models.TextField()
	
	
	def current_job(self):
		if self.end_date == datetime.date.today():
			return True
	
	
	def __unicode__(self):
		return self.user.username