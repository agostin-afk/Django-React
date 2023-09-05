# Generated by Django 4.2.3 on 2023-07-27 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Unidades', '0003_alter_subunidade_gestorsubunidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subunidade',
            name='gestorSubUnidade',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]