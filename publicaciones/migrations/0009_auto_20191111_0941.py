# Generated by Django 2.0.5 on 2019-11-11 15:41

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0008_auto_20191107_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='Tamaño recomendado: 360x390', null=True, upload_to='publicaciones/img/'),
        ),
    ]
