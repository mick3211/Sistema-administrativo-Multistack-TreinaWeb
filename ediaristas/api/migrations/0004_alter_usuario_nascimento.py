# Generated by Django 3.2.9 on 2022-05-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_usuario_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nascimento',
            field=models.DateField(),
        ),
    ]
