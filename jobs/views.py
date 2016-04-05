from django.shortcuts import render
from django.views.generic import View
from .models import Jobs
from rest_framework import generics
from .serializers import JobsSerializer
#from rest_framework import viewsets

# Create your views here.


class Index(View):
	def get(self,request, *args, **kwargs):
		params = dict()
		jobs = Jobs.objects.all()
		params["jobs"] = jobs
		return render(request, "index.html", params)

class Details(View):
	def get(self,request, *args, **kwargs):
		# Trarme los detalles mediante el slug, como argumento kwargs
		params = dict()
		slug = self.kwargs['slug']
		empleo = Jobs.objects.filter(slug=slug)
		print empleo
		params["empleo"] = empleo
		return render(request,"details.html", params)
		
class DetailsById(generics.RetrieveUpdateDestroyAPIView):
	queryset = Jobs.objects.all()
	serializer_class = JobsSerializer


'''
class JobsList(viewsets.ModelViewSet):
	queryset = Jobs.objects.all()
	serializer_class = JobsSerializer
'''
