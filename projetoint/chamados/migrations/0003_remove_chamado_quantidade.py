# Generated by Django 5.1.2 on 2024-11-21 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chamados', '0002_chamado_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamado',
            name='quantidade',
        ),
    ]