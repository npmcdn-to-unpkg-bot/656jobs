from .models import Jobs
from rest_framework import serializers


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = (
            'company',
            'title',
            'jobDescription',
            'skills',
            'postedDate',
            'salaryRange',
            'jobtype',
            'slug',
            'category',
            'user',
            'is_active',
        )


