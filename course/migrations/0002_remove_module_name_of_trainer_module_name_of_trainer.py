# Generated by Django 4.0.6 on 2022-07-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='name_of_trainer',
        ),
        migrations.AddField(
            model_name='module',
            name='name_of_trainer',
            field=models.ManyToManyField(to='trainer.trainer'),
        ),
    ]