from django.db import models

class LRNDKey(models.Model):
    key = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"LRND Key {self.id}"