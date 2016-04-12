from django.shortcuts import render
from django.views.generic import View
from .models import Jobs
from rest_framework import generics
from .serializers import JobsSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
#from rest_framework import viewsets

# Create your views here.

class Index(View):
	def get(self,request, *args, **kwargs):
		return render(request, "index.html")

class AllJobs(View):
	def get(self,request, *args, **kwargs):
		params = dict()
		jobs = Jobs.objects.all()
		params["jobs"] = jobs
		return render(request, "jobs.html", params)

class Details(View):
	def get(self,request, *args, **kwargs):
		# Trarme los detalles mediante el slug, como argumento kwargs
		params = dict()
		slug = self.kwargs['slug']
		empleo = Jobs.objects.filter(slug=slug)
		params["empleo"] = empleo
		return render(request,"details.html", params)

class Dashboard(LoginRequiredMixin,View):
	login_url = '/login/'
	def get(self, request, *args, **kwargs):
		return render(request, "dashboard.html")
		
		
class Login(View):
	def get(self, request, *args, **kwargs):
		return render(request, "login.html")
		
class DetailsById(generics.RetrieveUpdateDestroyAPIView):
	queryset = Jobs.objects.all()
	serializer_class = JobsSerializer
