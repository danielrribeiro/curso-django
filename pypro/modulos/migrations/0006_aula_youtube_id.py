# Generated by Django 4.1.3 on 2022-11-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='youtube_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
