# Generated by Django 5.1.2 on 2024-12-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produtos_tipo_de_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='nome',
            field=models.CharField(help_text='Nome completo do produto', max_length=100, verbose_name='Nome'),
        ),
    ]
