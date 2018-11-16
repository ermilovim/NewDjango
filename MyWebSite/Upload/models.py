from django.db import models

# Create your models here.


class NewIdForm(models.Model):

    identificator = models.CharField(max_length=100)
