# Generated by Django 2.0.2 on 2019-02-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='direccion',
            field=models.CharField(max_length=100, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='estadio',
            field=models.CharField(max_length=100, verbose_name='Estadio'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fundacion',
            field=models.IntegerField(verbose_name='Fundación'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(upload_to='equipos', verbose_name='Logotipo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='presidente',
            field=models.CharField(max_length=100, verbose_name='Presidente'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='puntos',
            field=models.IntegerField(verbose_name='Puntos'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='web',
            field=models.CharField(max_length=100, verbose_name='Página Web'),
        ),
    ]
