from django.db import models

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=30)
    s_std=models.IntegerField()
    s_div=models.CharField(max_length=20)

    class Meta:
        db_table='Student_db'

class Teacher(models.Model):
    student_id=models.ForeignKey('Student',on_delete=models.CASCADE,related_name='stud')
    tname=models.CharField(max_length=20)
    tsub=models.CharField(max_length=20)

    class Meta:
        db_table='Teacher_db'

# Create your models here.
