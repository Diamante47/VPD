# Generated by Django 5.1.3 on 2025-01-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventapasajes', '0004_alter_pasaje_unique_together_pasaje_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasaje',
            name='asiento',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='pasaje',
            unique_together={('horario', 'asiento')},
        ),
    ]
