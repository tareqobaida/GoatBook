from django.db import models


# Create your models here.
# If you need to create a relationship on a model that has not yet been defined,
# you can use the name of the model, rather than the model object itself
class List(models.Model):
    pass


class Item(models.Model):
    text=models.TextField(default='')
    list=models.ForeignKey(List, default=None)


