# Generated by Django 3.0 on 2021-12-08 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ods',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_ods'),
        ),
    ]
