# Generated by Django 4.2.3 on 2023-07-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gato',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
