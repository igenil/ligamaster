# Generated by Django 2.0.2 on 2019-02-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0005_auto_20190211_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadorperfil',
            name='capitan',
            field=models.BooleanField(default=False, verbose_name='Capitan'),
        ),
    ]
