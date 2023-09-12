from django.db import models
from django.contrib.auth.models import User
import uuid


class Person(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                           primary_key=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.name}"