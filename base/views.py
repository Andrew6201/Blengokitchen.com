from django.shortcuts import render,redirect
from .models import Person,FormSubmission,Image
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer ,FormSubmissionSerializer, ImageSerializer
# Create your views here.

#To get all my data for my menu
@api_view(['GET'])
def home(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people ,many = True)
    return Response(serializer.data)

#To get all my data in the About
@api_view(['GET'])
def about(request):
    people = Image.objects.all()
    serializer = ImageSerializer(people ,many = True)
    return Response(serializer.data)



@api_view(['POST'])
def order(request):
    serializer = FormSubmissionSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

