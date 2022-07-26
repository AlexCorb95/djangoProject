from django.db import models

from trainer.models import Trainer


class Module(models.Model):
    name_of_course = models.CharField(max_length=100)
    name_of_trainer = models.ManyToManyField(Trainer)
    course_duration = models.IntegerField()
    description = models.TextField(max_length=300)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name_of_course}'