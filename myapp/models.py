from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200,blank=True)
    photo = models.ImageField(upload_to="profile_image")
    qrcode = models.ImageField(upload_to="qrcode_image", blank=True)
    def __unicode__(self):
        return u"%s : %s"%(self.student_id,self.name)