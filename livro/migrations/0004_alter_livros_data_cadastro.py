# Generated by Django 5.0.1 on 2024-02-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_alter_livros_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
