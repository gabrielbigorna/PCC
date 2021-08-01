from django.db import models
from boxes.models import Box

# Create your models here.
class Page(models.Model):

    ident = models.OneToOneField(Box, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.ident.title;