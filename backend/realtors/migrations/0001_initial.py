# Generated by Django 3.2.7 on 2021-11-17 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('descrição', models.TextField(blank=True)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('mais_vendido', models.BooleanField(default=False)),
                ('data_contratacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]