# Generated by Django 5.0.1 on 2024-02-07 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_alter_emprestimos_data_devolucao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='tempo_duracao',
        ),
    ]