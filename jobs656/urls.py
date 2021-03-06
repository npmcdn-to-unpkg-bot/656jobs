'''
jobs656 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
'''
from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from jobs.views import Index, AllJobs, Details, DetailsById, Dashboard, Login, Logout, Register, UpdateProfile, Profiles, PublicProfile
from rest_framework.urlpatterns import format_suffix_patterns
from jobs import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view()),
    url(r'jobs/', AllJobs.as_view()),
    url(r'register/', Register.as_view()),
    url(r'dashboard/$', Dashboard.as_view()),
    url(r'job/\w+/(?P<slug>[\w-]+)/$', Details.as_view()),
    url(r'api/(?P<pk>[0-9]+)/$', DetailsById.as_view()),
    url(r'login/$', Login.as_view()),
    url(r'logout/$', Logout.as_view()),
    url(r'edit_profile/(?P<pk>[0-9]+)$', UpdateProfile.as_view()),
    url(r'profile/(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12})', Profiles.as_view(), name='profile'),
    url(r'profile/(?P<pk>[0-9]+)', Profiles.as_view()),
    url(r'candidate/(?P<uuid>[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12})',PublicProfile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)