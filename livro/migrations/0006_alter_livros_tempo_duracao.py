# Generated by Django 5.0.1 on 2024-02-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_alter_livros_data_cadastro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='tempo_duracao',
            field=models.DateField(blank=True, null=True),
        ),
    ]