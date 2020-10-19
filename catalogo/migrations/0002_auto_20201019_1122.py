# Generated by Django 2.0.5 on 2020-10-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivosproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Producto'),
        ),
        migrations.AlterField(
            model_name='fotosproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Producto'),
        ),
        migrations.AlterField(
            model_name='propuesta_valor',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Producto'),
        ),
    ]
