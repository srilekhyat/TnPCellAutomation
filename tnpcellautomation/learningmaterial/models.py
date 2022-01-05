from django.db import models
from PIL import Image
import uuid

# Create your models here.
class Concept(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    concept = models.CharField(verbose_name="Concept", max_length=100)
    image = models.ImageField(default="defaultprofilepic.jpg", upload_to="learningmaterial")

    def save(self, *args, **kwargs):
        super(Concept, self).save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image

class Topic(models.Model):
    concept = models.ForeignKey(Concept, verbose_name="Concept", max_length=100, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    topic = models.CharField(verbose_name="Topic", max_length=100)
    title1 = models.CharField(verbose_name="Title1", max_length=500)
    description1 = models.CharField(verbose_name="Description1", max_length=3000)
    title2 = models.CharField(verbose_name="Title2", max_length=500)
    description2 = models.CharField(verbose_name="Description2", max_length=3000)
    title3 = models.CharField(verbose_name="Title3", max_length=500)
    description3 = models.CharField(verbose_name="Description3", max_length=3000)