from django.db import models
from django.contrib.auth.models import User


class Schema(models.Model):

    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, related_name='schemas', on_delete=models.CASCADE)


class SchemaColumn(models.Model):

    name = models.CharField(max_length = 30)
    datatype = models.CharField(max_length = 50)
    order = models.IntegerField()
    schema = models.ForeignKey(Schema, related_name='columns', on_delete=models.CASCADE)
