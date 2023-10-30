from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import generics, status, mixins, viewsets
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import permissions
from . import serializers
from ..models import *


class CompanyViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        serializer = serializers.CompanySerializer(companies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {

        }
        serializer = serializers.CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Company does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = {

        }
        serializer = serializers.CompanySerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Company does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({'data': 'Company was deleted from system.'},
                        status=status.HTTP_200_OK)


class JobViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def get_objcet(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        serializer = serializers.JobListSerializer(jobs, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {

        }
        serializer = serializers.JobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        instance = self.get_objcet(pk)
        if not instance:
            return Response({'data': 'Job does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = {

        }
        serializer = serializers.JobSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_objcet(pk)
        if not instance:
            return Response({'data': 'Job does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({'data': 'Job was deleted from system.'},
                        status=status.HTTP_200_OK)