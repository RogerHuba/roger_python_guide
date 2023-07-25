from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

class Posts(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    title = models.CharField(max_length=64)
    body = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.title

