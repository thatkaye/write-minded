from django.db import models

# for upload file
# Create your models here.
class uploadfilemodel(models.Model):
    file = models.FileField()