# Generated by Django 4.0.6 on 2022-08-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
