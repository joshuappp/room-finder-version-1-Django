from django.db import models

# Create your models here.
class FindRoom(models.Model):

    province = models.CharField(max_length=30,blank=False,null=False)
    location = models.CharField(max_length=40,blank=False,null=False)
    section  = models.CharField(max_length=40,blank=False,null=False)

class UploadRoom(models.Model):

    province = models.CharField(max_length=30,blank=False,null=False)
    location = models.CharField(max_length=40,blank=False,null=False)
    section  = models.CharField(max_length=40,blank=False,null=False)
    address  = models.CharField(max_length=60,blank=False,null=False)
    price    = models.DecimalField(decimal_places=2,max_digits=10,blank=False,null=False)
    contact  = models.IntegerField(blank=False,null=False)
    image    = models.ImageField(blank=False,null=False)



class ContactUs(models.Model):

	fullname    = models.CharField(max_length=60,blank=False,null=False)
	contact     = models.IntegerField(blank=False,null=False)
	email       = models.EmailField(max_length=50,blank=False,null=False)
	description = models.CharField(max_length=100,blank=True,null=True)


		
