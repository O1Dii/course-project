# Generated by Django 2.2.1 on 2019-05-16 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20190513_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
