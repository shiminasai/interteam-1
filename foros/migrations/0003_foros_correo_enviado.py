# Generated by Django 2.0.5 on 2019-11-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foros', '0002_auto_20180828_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='foros',
            name='correo_enviado',
            field=models.BooleanField(default=True, editable=False),
            preserve_default=False,
        ),
    ]
