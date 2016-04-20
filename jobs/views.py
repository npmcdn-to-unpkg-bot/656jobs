from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Jobs, Profile, WorkExperience
from rest_framework import generics
from .serializers import JobsSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, EditProfile, WorkExperienceForm
from utils import username_exists
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


#from rest_framework import viewsets

# Create your views here.
# Favor de crear las vistas con nombres detallados para que no colisionen con los modelos

class Index(View):
	def get(self,request, *args, **kwargs):
		return render(request, "index.html")
class AllJobs(View):
	def get(self,request, *args, **kwargs):
		params = {}
		jobs = Jobs.objects.all()
		params["jobs"] = jobs
		return render(request, "jobs.html", params)
class Details(View):
	def get(self,request, *args, **kwargs):
		# Trarme los detalles mediante el slug, como argumento kwargs
		params = {}
		slug = self.kwargs['slug']
		empleo = Jobs.objects.filter(slug=slug)
		params["empleo"] = empleo
		return render(request,"details.html", params)
class Dashboard(LoginRequiredMixin,View):
	login_url = '/login/'
	template_name = 'dashboard.html'
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
class Profiles(View):
	template_name = 'profile.html'
	work_experience_form = WorkExperienceForm
	
	def get(self, request, *args, **kwargs):
		userid = User.objects.get(username=request.user)
		userid = userid.id
		work_experience = WorkExperience.objects.all().filter(user_id=userid)
		form = self.work_experience_form
		params = dict()
		params["works"] = work_experience
		params["form"] = form
		return render(request, self.template_name, params)
		
	def post(self,request,*args,**kwargs):
		user = WorkExperience(user=request.user)
		form = self.work_experience_form(request.POST,instance=user)
		if form.is_valid():
			add_work = form.save(commit=False)
			add_work.save()
			return redirect('/profile')
		else:
			print "La forma no es valida"
			return redirect('/profile')
			
class Login(View):
	login_form = UserForm
	
	def get(self, request, *args, **kwargs):
		form = self.login_form
		params = {}
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
				error = "Lo siento tu usuario o password son incorrectos"
				params = {}
				form = self.login_form
				params["form"] = form
				params["error"] = error
		return render(request,"login.html", params)
class Logout(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return redirect('/')			
class Register(View):
	register_form = UserForm
	
	def get(self, request, *args, **kwargs):
		form = self.register_form
		params = {}
		params["form"] = form
		return render(request, "register.html", params)
	
	def post(self, request, *args, **kwargs):
		if request.POST:
			form = self.register_form(request.POST)
			username = request.POST['username']
			user_exist = username_exists(username)
			if user_exist:
				error = "Ya existe este usuario elige otro"
				params = {}
				params["form"] = form
				params["error"] = error
				return render(request,"register.html", params)
			else:
				if form.is_valid():
					# cleaned (normalized) data
					user = form.save(commit=False)
					username = form.cleaned_data['username']
					password = form.cleaned_data['password']
					user.set_password(password)
					user.save()
					
					#returns the User objects if credentials are correct
					user = authenticate(username=username,password=password)
					if user is not None and user.is_active:
						login(request,user)
						return redirect('/dashboard')
				else:
					params = dict()
					params["error"] = form.errors
					params["form"] = form
					return render(request,"register.html", params)
class DetailsById(generics.RetrieveUpdateDestroyAPIView):
	queryset = Jobs.objects.all()
	serializer_class = JobsSerializer
class UpdateProfile(View):
	template_name = "update_profile.html"
	profile_form = EditProfile
	
	def get(self, request, *args, **kwargs):
		
		try:
			profile = request.user.profile
		except Profile.DoesNotExist:
			profile = Profile(user=request.user)
		
		form = self.profile_form(instance=profile)	
		params = dict()
		params["form"] = form
		return render(request, self.template_name, params)
		
	
	def post(self, request, *args, **kwargs):
		
		try:
			profile = request.user.profile
		except Profile.DoesNotExist:
			profile = Profile(user=request.user)
			
		form = self.profile_form(request.POST,request.FILES, instance=profile)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('profile', args=[request.user.profile.uuid ]))
		
		else:
			params = dict()
			params["error"] = form.errors
			params["form"] = form
			return render(request, self.template_name, params)
