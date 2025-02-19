# Generated by Django 5.1.3 on 2024-12-04 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("formulario", "0002_rename_publicacion_oferta"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="criterioinclusion",
            name="banos_accesibles",
        ),
        migrations.RemoveField(
            model_name="criterioinclusion",
            name="elevadores",
        ),
        migrations.RemoveField(
            model_name="criterioinclusion",
            name="espacios_trabajo_adaptados",
        ),
        migrations.RemoveField(
            model_name="criterioinclusion",
            name="politica_inclusion_laboral",
        ),
        migrations.RemoveField(
            model_name="criterioinclusion",
            name="rampas_acceso",
        ),
        migrations.AddField(
            model_name="criterioinclusion",
            name="criterio",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="criterioinclusion",
            name="descripcion_criterio",
            field=models.TextField(blank=True, null=True),
        ),
    ]
