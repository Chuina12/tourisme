# Generated by Django 5.1.2 on 2024-11-14 03:16

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourisme_app', '0016_delete_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='activity')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='BaniereDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='banieredestination')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='destination')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('activities', models.ManyToManyField(related_name='destinations', to='tourisme_app.activity')),
                ('baniereDestination', models.ManyToManyField(related_name='destinations', to='tourisme_app.banieredestination')),
            ],
        ),
    ]