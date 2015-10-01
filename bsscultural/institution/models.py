from django.db import models
from bsscultural.course.models import Course

class Institution(models.Model):
    name = models.TextField()
    affiliation_no = models.CharField(max_length=25,unique=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)   
    address = models.CharField(max_length=1024,blank=True,null=True)
    mobile = models.CharField(max_length=100,blank=True,null=True)
    Landphone = models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    #temp_id = models.CharField(blank=True,null=True,max_length=10) 
    
    def __unicode__(self):
        return self.name
    
class Institution_Courses(models.Model):
    institution = models.ForeignKey(Institution)
    course = models.ForeignKey(Course)
    
    def __unicode__(self):
        return str(self.institution.name) + ' ---> ' + str(self.course.name)