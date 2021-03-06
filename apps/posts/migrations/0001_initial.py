# Generated by Django 3.0 on 2021-12-08 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes_posts')),
                ('Ods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Ods')),
            ],
        ),
    ]
