# Generated by Django 2.0.2 on 2019-02-16 16:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torneos', '0005_auto_20190212_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torneo',
            name='descripcion',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Descripcion'),
        ),
    ]
