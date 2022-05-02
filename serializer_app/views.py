from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
# Model Object -single student data
'''
def student_detail(request):
    stu = Student.objects.get(id=1) #complex data
    serializer = StudentSerializer(stu) #change to python object
    json_data = JSONRenderer().render(serializer.data) #python object convert to json
    # now send the json data
    return HttpResponse(json_data,content_type='application/json')
'''
#id pass from url
def student_detail(request,pk):
    stu = Student.objects.get(id=pk) #complex data
    serializer = StudentSerializer(stu) #change to python object
    json_data = JSONRenderer().render(serializer.data) #python object convert to json
    # now send the json data
    return HttpResponse(json_data,content_type='application/json')


#Query set -all student data

def student_list(request):
    stu = Student.objects.all() #complex data
    serializer = StudentSerializer(stu, many=True) #change to python object
    json_data = JSONRenderer().render(serializer.data) #python object convert to json
    # now send the json data
    return HttpResponse(json_data,content_type='application/json')