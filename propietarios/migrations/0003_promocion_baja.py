# Generated by Django 4.0.5 on 2022-09-02 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propietarios', '0002_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='baja',
            field=models.BooleanField(default=0),
        ),
    ]
