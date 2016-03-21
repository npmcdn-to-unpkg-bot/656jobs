from django.contrib import admin
from .models import Jobs
# Register your models here.

class JobsAdmin(admin.ModelAdmin):
	prepopulated_fields = { "slug" : ("title",)}

admin.site.register(Jobs,JobsAdmin)
