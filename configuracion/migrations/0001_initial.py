# Generated by Django 2.0.5 on 2018-06-26 17:10

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.CharField(max_length=150)),
                ('imagen', sorl.thumbnail.fields.ImageField(help_text='720x440', upload_to='banner-index/')),
            ],
            options={
                'verbose_name': 'Banner Index',
                'verbose_name_plural': 'Banner Index',
            },
        ),
    ]