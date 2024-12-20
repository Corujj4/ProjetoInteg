# Generated by Django 5.1.2 on 2024-12-10 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lista', '0001_initial'),
        ('produtos', '0011_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaProdutos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0, verbose_name='quantidade')),
                ('lista', models.ForeignKey(help_text='nome da lista', on_delete=django.db.models.deletion.CASCADE, related_name='lista', to='lista.lista', verbose_name='lista')),
                ('produto', models.ForeignKey(help_text='nome da produto', on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='produtos.produtos', verbose_name='produto')),
            ],
            options={
                'verbose_name': 'lista de produtos',
                'verbose_name_plural': 'listas de produtos',
                'ordering': ['quantidade'],
            },
        ),
    ]
