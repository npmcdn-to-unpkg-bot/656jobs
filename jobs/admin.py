from django.contrib import admin
from .models import Company, Jobs, Category
from company_profile.models import CompanyUser

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('company','companyWebsite')

class JobsAdmin(admin.ModelAdmin):
	prepopulated_fields = { "slug" : ("title",)}
	list_display = ('title','postedDate','company')


admin.site.register(Company,CompanyAdmin)
admin.site.register(Jobs,JobsAdmin)
admin.site.register(Category)
admin.site.register(CompanyUser)

