# Generated by Django 5.2 on 2025-04-12 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epi_app', '0005_rename_colaborador_controle_colaborador_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controle',
            old_name='colaborador_id',
            new_name='colaborador',
        ),
        migrations.RenameField(
            model_name='controle',
            old_name='equipamento_id',
            new_name='equipamento',
        ),
    ]
