from django.shortcuts import render
from django.views.generic import View
from .models import Jobs
# Create your views here.


class Index(View):
	def get(self,request, *args, **kwargs):
		params = dict()
		jobs = Jobs.objects.all()
		params["jobs"] = jobs
		return render(request, "index.html", params)

class Details(View):
	def get(self,request, *args, **kwargs):
		''' Trarme los detalles mediante el slug, como argumento kwargs '''
		params = dict()
		slug = self.kwargs['slug']
		empleo = Jobs.objects.filter(slug=slug)
		print empleo
		params["empleo"] = empleo
		return render(request,"details.html", params)