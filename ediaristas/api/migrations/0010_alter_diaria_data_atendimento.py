# Generated by Django 3.2.9 on 2022-06-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_diaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaria',
            name='data_atendimento',
            field=models.DateTimeField(),
        ),
    ]
