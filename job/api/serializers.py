from rest_framework import serializers
from job.models import *


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobType
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class CompanyTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyType
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class JobListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            'salary',
        ]


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'













