# Generated by Django 4.0.6 on 2022-07-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('is_olympic', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
