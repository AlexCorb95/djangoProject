from django.db import models


class Trainer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
