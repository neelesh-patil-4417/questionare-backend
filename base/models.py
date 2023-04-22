from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class quizdata(models.Model):
    question = models.TextField(max_length=500)
    answer = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question