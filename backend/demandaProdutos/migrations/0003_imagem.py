# Generated by Django 4.2.4 on 2023-10-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demandaProdutos', '0002_delete_arquivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
