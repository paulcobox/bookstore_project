from django.db import models

# Create your models here.


# Create your models here.

class LegalBaseModel(models.Model):
  created = models.DateTimeField('created at', auto_now_add=True, help_text='Date time on which the object was created.')
  updated = models.DateTimeField('updated at', auto_now=True, help_text='Date time on which the object was updated.')

  class Meta:
    abstract = True
    get_latest_by = 'created'
    ordering = ['-created', '-updated']