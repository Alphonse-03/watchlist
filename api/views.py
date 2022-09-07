from django.shortcuts import render
from django.http import JsonResponse
from api.serializers import MovieSerializer,StreamPlatformSerializer
from api.models import Movie,StreamPlatform
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# @api_view(['GET','POST'])
# def stream(request):
#     if request.method == 'GET':
#         movies=StreamPlatform.objects.all()
#         serializer=StreamPlatformSerializer(movies,many=True)

#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer=StreamPlatformSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class Stream(APIView):
  
    def get(self, request, format=None):
        movies=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(movies,many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer=StreamPlatformSerializer(data=request.data)      
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
       





@api_view(['GET','POST'])
def home(request):
    if request.method == 'GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer=MovieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def movies(request,pk):
    if request.method == 'GET':
        movies=Movie.objects.filter(director=pk)
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)

   



@api_view(['GET','PUT','DELETE'])
def post(request,pk):
    if request.method == 'GET':
        try:
            val=Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serial=MovieSerializer(val)
        return Response(serial.data)
    
    if request.method == 'PUT':
        val=Movie.objects.get(id=pk)
        serializer=MovieSerializer(val,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        val=Movie.objects.get(id=pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    