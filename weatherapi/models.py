from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=50,blank=False)
    email= models.EmailField(max_length=50,blank=False)
    username = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=50,blank=False)
    mobileno = models.IntegerField(max_length=50,blank=False)
    location = models.CharField(max_length=50,blank=False)
    class Meta:
        db_table = "WeatherApi_table"


class FeedBackForm(models.Model):
    suggestion=models.CharField(blank=False)

class stars(models.Model):
    stars=models.IntegerField(max_length=5,blank=False)
    class Meta:
        db_table="FeedBack_Stars_Table"
class UserFeedBack(models.Model):
    suggestion = models.CharField(blank=False)
    stars=models.IntegerField(max_length=5,blank=False)
    name=models.CharField(max_length=15,blank=False)
    class Meta:
        db_table="User_FeedBack_Form"
