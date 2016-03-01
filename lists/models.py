from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
# If you need to create a relationship on a model that has not yet been defined,
# you can use the name of the model, rather than the model object itself
class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text=models.TextField(default='')
    list=models.ForeignKey(List, default=None)


