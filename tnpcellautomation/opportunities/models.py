from django.db import models
import uuid
from django.db.models.fields.related import ManyToManyField
from django.utils import timezone
from user.models import User

# Create your models here.
class Opportunity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.TextField(max_length=50, verbose_name="Title", default="None")
    company_name = models.TextField(max_length=50, verbose_name="Company Name", default="None")
    description = models.TextField(max_length=150, verbose_name="Description", default="None")
    eligibility = models.TextField(max_length=50, verbose_name="Eligibility", default="None")
    link_to_apply = models.TextField(max_length=1000, verbose_name="Link", default="None")
    is_hackathon = models.BooleanField(default=False)
    is_job = models.BooleanField(default=False)
    is_internship = models.BooleanField(default=False)

class Interested(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)