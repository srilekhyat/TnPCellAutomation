from django.db import models
from user.models import User
import uuid

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    ques = models.CharField(verbose_name="Question", max_length=1000)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.CharField(verbose_name="Answer", max_length=2000)