# Generated by Django 5.0.1 on 2024-02-22 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_alter_emprestimos_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='capa_livro'),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 22, 12, 24, 23, 489165)),
        ),
    ]
