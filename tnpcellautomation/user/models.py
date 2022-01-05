from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default="defaultprofilepic.jpg", upload_to="profile_pics")
    rollno = models.TextField(max_length=15, verbose_name="Roll No.")
    firstname = models.TextField(max_length=50, verbose_name="First Name")
    lastname = models.TextField(max_length=50, verbose_name="Last Name")
    emailid = models.EmailField(verbose_name="Email ID: ", max_length=150)
    User.is_student = True

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="defaultprofilepic.jpg", upload_to="profile_pics")
    staffid = models.TextField(max_length=50, verbose_name="Staff ID")
    firstname = models.TextField(max_length=50, verbose_name="First Name")
    lastname = models.TextField(max_length=50, verbose_name="Last Name")    
    emailid = models.EmailField(verbose_name="Email ID")
    User.is_professor = True

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image