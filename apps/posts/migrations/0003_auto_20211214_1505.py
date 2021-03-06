# Generated by Django 3.0 on 2021-12-14 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_ods_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-fecha_post']},
        ),
        migrations.RemoveField(
            model_name='posts',
            name='Titulo',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='posts',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='fecha_post',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ods',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
