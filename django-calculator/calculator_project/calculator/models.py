from django.db import models
from django.utils import timezone

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.expression} = {self.result}"