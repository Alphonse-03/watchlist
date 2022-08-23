from django.shortcuts import render
from django.http import JsonResponse
from api.serializers import MovieSerializer
from api.models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

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
    