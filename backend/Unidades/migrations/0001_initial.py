# Generated by Django 4.2.3 on 2023-07-27 16:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubUnidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('endereco', models.TextField()),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('departamento', models.CharField(max_length=100)),
                ('GestorUnidade', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('subunidades', models.ManyToManyField(blank=True, to='Unidades.subunidade')),
            ],
        ),
    ]
