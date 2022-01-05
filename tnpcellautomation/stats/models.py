from django.db import models
from PIL import Image

# Create your models here.
class Graph(models.Model):
    image = models.ImageField(upload_to='graphs')