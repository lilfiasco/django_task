# Generated by Django 4.1.3 on 2022-12-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='почта'),
        ),
    ]