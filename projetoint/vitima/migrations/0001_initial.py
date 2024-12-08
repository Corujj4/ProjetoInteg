# Generated by Django 5.1.2 on 2024-12-08 02:49

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vitima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome Completo', max_length=50, verbose_name='nome')),
                ('fone', models.CharField(help_text='Numero de Telefone', max_length=15, verbose_name='fone')),
                ('email', models.EmailField(help_text='Endereço de E-mail', max_length=100, unique=True, verbose_name='E-mail')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pessoas', variations={}, verbose_name='Foto')),
                ('idade', models.IntegerField(help_text='Idade', verbose_name='Idade')),
                ('necessidade', models.CharField(help_text='Descricao de necessidade', max_length=100, verbose_name='Necessidade')),
            ],
            options={
                'verbose_name': 'vitima',
                'verbose_name_plural': 'vitimas',
            },
        ),
    ]
