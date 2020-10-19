from django.db import models

# Create your models here.
class Adopt(models.Model):
   name = models.CharField(max_length=50)
   email = models.EmailField(max_length=100)
   phone = models.CharField(max_length=10, blank=True ,null=True)
   mes = models.CharField(max_length=200,blank=True ,null=True)
   doc = models.CharField(max_length=30, blank=True ,null=True)
   pictures = models.ImageField(upload_to='pictures')

   def __str__(self):
      return self.name


class meta:
   db_table="adopt"


class camp(models.Model):
   title = models.CharField(max_length=100)
   venue = models.CharField(max_length=100)
   time = models.CharField(max_length=10)
   date = models.CharField(max_length=10,default='')
   month= models.CharField(max_length=10,default='')
   description = models.CharField(max_length=500)
   img = models.ImageField(upload_to='pictures')

   def __str__(self):
      return self.title


class profile(models.Model):
   usname = models.CharField(max_length=50,default='')
   title = models.CharField(max_length=100)
   venue = models.CharField(max_length=100)
   date = models.CharField(max_length=10,default='')
   month= models.CharField(max_length=10,default='')
   time = models.CharField(max_length=10)

   def __str__(self):
      return self.title

class order(models.Model):
   usname = models.CharField(max_length=50,default='')
   title = models.CharField(max_length=100)
   venue = models.CharField(max_length=100)
   quant = models.CharField(max_length=10)

   def __str__(self):
      return self.title