# Ex02 Django ORM Web Application
## Date: 28-02-2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![ER DIAGRAM](<er diagram.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM:
```
from django.db import models
from django.contrib import admin
class Bookdetails(models.Model):
   Studentname=models.CharField(max_length=20);
   Regno=models.IntegerField();
   BookName=models.CharField(max_length=50);
   AuthorName=models.CharField(max_length=50);
   BookNo=models.IntegerField(primary_key=True);
   YearofRelease=models.DateField();
   Totalpage=models.IntegerField();
   
class BookdetailsAdmin(admin.ModelAdmin):
   list_display=("Studentname","Regno","BookName","AuthorName","AuthorName","BookNo","YearofRelease","Totalpage");

from django.contrib import admin
from .models import Bookdetails,BookdetailsAdmin
admin.site.register(Bookdetails,BookdetailsAdmin)
```
## OUTPUT:
![alt text](output.jpg)
## RESULT
Thus the program for creating a database using ORM hass been executed successfully
