# Generated by Django 4.1.4 on 2022-12-12 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='fim',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='turma',
            name='inicio',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turmas.turma')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='turma',
            name='alunos',
            field=models.ManyToManyField(through='turmas.Matricula', to=settings.AUTH_USER_MODEL),
        ),
    ]
