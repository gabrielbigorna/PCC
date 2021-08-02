from django.db import models
from django.contrib.auth import get_user_model
from pages.models import Page

# Create your models here.
class File(models.Model):

    STATUS = (
        ("fazendo", "Fazendo"),
        ("finalizado", "finalizado"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.CharField(
        max_length=10,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title;