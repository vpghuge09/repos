from django.shortcuts import render
from .serializers import Studentserializer,Teacherserializer
from rest_framework.viewsets import ModelViewSet
from .models import Student,Teacher
class StudentApi(ModelViewSet):
    serializer_class = Studentserializer
    queryset = Student.objects.all()

class TeacherApi(ModelViewSet):
    serializer_class = Teacherserializer
    queryset = Teacher.objects.all()



# Create your views here.
