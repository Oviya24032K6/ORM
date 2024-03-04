# Create your models here.
from django.db import models
from django.contrib import admin
class Bookdetails(models.Model):
   Studentname=models.CharField(Max_length=20);
   Regno=models.models.IntegerField();
   BookName=models.CharField(Max_length=50);
   AuthorName=models.CharField(Max_length=50);
   BookNo=models.IntegerField(primary_key=True);
   YearofRelease=models.DateField();
   Totalpage=models.IntegerField();
   
class BookdetailsAdmin(admin.ModelAdmin):
   list_display=("Studentname","Regno","BookName","AuthorName","AuthorName","BookNo","YearofRelease","Totalapge");
