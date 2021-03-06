# Generated by Django 2.0.5 on 2019-11-07 15:44

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('archivo', models.FileField(upload_to='informes/archivos/')),
            ],
        ),
        migrations.CreateModel(
            name='HistoriasExito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='informes/historias-exito/')),
                ('texto', models.TextField()),
            ],
            options={
                'verbose_name': 'Historia de éxito',
                'verbose_name_plural': 'Historias de éxito',
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('archivo', sorl.thumbnail.fields.ImageField(upload_to='informes/imgenes/')),
            ],
            options={
                'verbose_name': 'Imágen',
                'verbose_name_plural': 'Imágenes',
            },
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_reporte', models.CharField(choices=[('Informe técnico', 'Informe técnico'), ('Informe financiero', 'Informe financiero')], max_length=50)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('fecha_informe', models.DateField()),
                ('archivo', models.FileField(upload_to='informes/informe/')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('objectivos', ckeditor_uploader.fields.RichTextUploadingField()),
                ('descripcion', ckeditor_uploader.fields.RichTextUploadingField()),
                ('coordinador_proyecto', models.CharField(max_length=300, verbose_name='Coordinador general del proyecto')),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=50)),
                ('responsable_proyecto', models.CharField(max_length=300)),
                ('slug', models.SlugField(editable=False, max_length=320)),
                ('url_para_compartir', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('url', embed_video.fields.EmbedVideoField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.Proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='informe',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.Proyecto'),
        ),
        migrations.AddField(
            model_name='imagenes',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.Proyecto'),
        ),
        migrations.AddField(
            model_name='historiasexito',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.Proyecto'),
        ),
        migrations.AddField(
            model_name='archivo',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.Proyecto'),
        ),
    ]
