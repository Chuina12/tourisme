# Generated by Django 5.1.2 on 2024-10-10 09:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourisme_app', '0002_service_image_couverture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=100)),
                ('titre', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Présentation',
                'verbose_name_plural': 'Présentations',
            },
        ),
    ]