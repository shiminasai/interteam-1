# Generated by Django 2.0.5 on 2019-11-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0006_auto_20180823_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='correo_enviado',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='publicada',
            field=models.BooleanField(default=True, editable=False),
            preserve_default=False,
        ),
    ]
