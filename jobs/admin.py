from django.contrib import admin
from .models import Jobs, Category
# Register your models here.

class JobsAdmin(admin.ModelAdmin):
	prepopulated_fields = { "slug" : ("title",)}
	list_display = ('title','postedDate','company')

admin.site.register(Jobs,JobsAdmin)
admin.site.register(Category)
