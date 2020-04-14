import re
import string
import uuid
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from django.db import models

# Create your models here.
class CustomUrl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_in = models.DurationField(null=True, blank=True)
    content_type = models.Foreignkey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    for_object = GenericForeignKey()
    url = models.URLField()
    url_type = models.CharField(
        max_length=10,
        choices=(("SHORT", "SHORTENED URL"), ("FRONTEND", "FRONTEND URL")),
    )
    description = models.TextField(default="")

    class Meta:
        unique_together = ("content_type", "object_id", "url_type")

        def __str__(self):
            return str(self.url)
