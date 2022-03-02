from django.db import models


# Create your models here.

class quesmodel(models.Model):
    # objects = None
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    option4 = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)

    def __str__(self):
        return self.question
