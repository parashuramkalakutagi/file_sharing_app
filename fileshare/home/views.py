from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import FileListSerializer
from .models import *
from rest_framework import status



class FileShareView(viewsets.ViewSet):

    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                
                response_data = {
                    "data":serializer.data,
                    "message": "Files uploaded successfully.",
                    "status_code": status.HTTP_201_CREATED
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                response_data = {
                    "error": serializer.errors,
                    "message": "Invalid data format.",
                    "status_code": status.HTTP_400_BAD_REQUEST
                }
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        except KeyError as e:
            response = {
                "error": str(e),
                "message": "Invalid data format.",
                "status_code": status.HTTP_400_BAD_REQUEST
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            response = {
                "error": str(e),
                "message": "Something went wrong.",
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)