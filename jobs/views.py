from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Jobs
from rest_framework import generics
from .serializers import JobsSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import UserForm
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
	login_form = UserForm
	
	def get(self, request, *args, **kwargs):
		form = self.login_form
		params = dict()
		params["form"] = form
		return render(request, "login.html", params)
	
	def post(self, request, *args, **kwargs):
		if request.POST:
			username = request.POST['username']
			password = request.POST['password']
			#returns the User objects if credentials are correct
			user = authenticate(username=username,password=password)
			if user is not None and user.is_active:
				login(request,user)
				return redirect('/dashboard')
			else: 
				# Return invalid login message
				error = "Lo siento tu usuario o password son incorrectos!"
				params = dict()
				form = self.login_form
				params["form"] = form
				params["error"] = error
		return render(request,"login.html", params)
			
	
class Register(View):
	register_form = UserForm
	
	def get(self, request, *args, **kwargs):
		form = self.register_form
		params = dict()
		params["form"] = form
		return render(request, "register.html", params)
	
	def post(self, request, *args, **kwargs):
		form = self.register_form(request.POST)
		if form.is_valid():
			# cleaned (normalized) data
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			
			#returns the User objects if credentials are correct
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('/dashboard')
		
class DetailsById(generics.RetrieveUpdateDestroyAPIView):
	queryset = Jobs.objects.all()
	serializer_class = JobsSerializer
