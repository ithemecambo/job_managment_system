from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from candidate.models import *
from . import serializers


class CandidateViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def get_object(self, pk):
        try:
            return Candidate.objects.get(pk=pk)
        except Candidate.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        candidates = Candidate.objects.all()
        serializer = serializers.CandidateSerializer(candidates, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {

        }
        serializer = serializers.CandidateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Candidate does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = {

        }
        serializer = serializers.CandidateSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Candidate does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({'data': 'Candidate was deleted from system.'},
                        status=status.HTTP_200_OK)


class ExperienceViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        experiences = Experience.objects.all()
        serializer = serializers.ExperienceSerializer(experiences)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EducationLevelViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]


class PortfolioViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]



