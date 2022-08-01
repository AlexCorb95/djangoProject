from django.db import models

from trainer.models import Trainer


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    is_olympic = models.BooleanField(default=False)
    address = models.CharField(max_length=150)
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Credits(models.Model):
    name_of_exam = models.CharField(max_length=100) # blank=True pentru a nu fi obligatoriu campul
    no_of_credits = models.IntegerField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_of_exam}'
