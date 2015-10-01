from django.db import models

class Course(models.Model):
    temp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=1024)
    duration = models.CharField(max_length=10)
    eligibility = models.CharField(max_length=50,null=True,blank=True)
    total_fee = models.CharField(max_length=10, null=True, blank=True)
    Reg_fee = models.CharField(max_length=10, null=True, blank=True)
    exam_fee = models.CharField(max_length=10, null=True, blank=True)
    no_of_exams = models.CharField(max_length=10)
    is_active = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
class Subject_Heading(models.Model):
    course = models.ForeignKey(Course)
    exam_no = models.CharField(max_length=10)
    heading= models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.heading

class Subject(models.Model):
    course = models.ForeignKey(Course)
    heading = models.ForeignKey(Subject_Heading)
    name = models.CharField(max_length=200)
    max_mark = models.IntegerField()
    min_mark = models.IntegerField()
    is_theory = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
class Paper(models.Model):
    subject = models.ForeignKey(Subject)
    paper = models.CharField(max_length=1024)