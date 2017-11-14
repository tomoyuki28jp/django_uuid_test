import uuid
from django.db import models

class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()

    def __str__(self):
       return self.body

    class Meta:
        verbose_name = '投稿'
        verbose_name_plural = '投稿'
