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
