from django.db import models
from django.contrib.auth import get_user_model
from boxes.models import Box

# Create your models here.
class Page(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ident = models.OneToOneField(Box, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.ident.title;