from django.db import models
from bsscultural.institution.models import *
from bsscultural.course.models import *
 
class Student(models.Model):
    name = models.CharField(max_length=1024)
    reg_no = models.CharField(max_length=10)
    institution = models.ForeignKey(Institution)
    course = models.ForeignKey(Course)
    gender = models.CharField(max_length=10,blank=True,null=True)
    age = models.CharField(max_length=5,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    guardian_name = models.CharField(max_length=1024, null=True, blank=True)
    duration = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=1024,blank=True,null=True)
    mobile = models.CharField(max_length=15,blank=True,null=True)
    Landphone = models.CharField(max_length=15,blank=True,null=True)
    marklist_status = models.BooleanField()
    certificate_status = models.BooleanField()
    
    def __unicode__(self):
        return self.name

class Marklist(models.Model):
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    mark = models.IntegerField()
    exam_no = models.CharField(max_length=2)

    def __unicode__(self):
        return self.subject.name