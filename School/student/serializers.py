
from rest_framework.serializers import ModelSerializer
from .models import Student,Teacher

class Studentserializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class Teacherserializer(ModelSerializer):
    class Meta:
        model= Teacher
        fields='__all__'





