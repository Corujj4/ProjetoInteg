# Generated by Django 5.1.2 on 2024-12-10 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0002_lista_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='produto',
        ),
    ]