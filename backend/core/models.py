from pickletools import uint1
from pyexpat import model
import uuid
from django.db import models

from versatileimagefield.fields import VersatileImageField


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]