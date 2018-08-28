# Generated by Django 2.0.5 on 2018-08-28 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aportes',
            name='foro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Foros'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='aporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Aportes'),
        ),
    ]
