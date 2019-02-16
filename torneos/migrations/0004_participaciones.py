# Generated by Django 2.0.2 on 2019-02-12 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0005_auto_20190211_0900'),
        ('torneos', '0003_auto_20190211_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField(blank=True, null=True)),
                ('equipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='equipo', to='equipos.Equipo', verbose_name='Equipo')),
                ('torneo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='torneo', to='torneos.Torneo', verbose_name='Torneo')),
            ],
        ),
    ]
