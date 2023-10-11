from django.db import models
from datetime import datetime

# Define the FormSubmission model
class FormSubmission(models.Model):
    firstname = models.CharField(max_length=200)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.firstname

# Define the Person model separately
class Person(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    content = models.TextField()
    school = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to="images/")  # Assuming you want to store the actual image file
    description = models.TextField(blank=True)  # Optional description for the image

    def __str__(self):
        return self.description
