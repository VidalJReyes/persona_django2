# Generated by Django 4.2 on 2023-04-04 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_domicilio_personas_domicilio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domicilio',
            name='pais',
        ),
    ]