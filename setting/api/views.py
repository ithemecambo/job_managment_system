from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import *
from setting.models import *
from . import serializers


class BlogViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, FileUploadParser]

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = serializers.BlogSerializer(blogs)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {

        }
        serializer = serializers.BlogSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Blog does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        data = {

        }
        serializer = serializers.BlogSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if not instance:
            return Response({'data': 'Blog does not existing.'},
                            status=status.HTTP_400_BAD_REQUEST)

        instance.delete()
        return Response({'data': 'Blog was deleted from system.'},
                        status=status.HTTP_200_OK)
