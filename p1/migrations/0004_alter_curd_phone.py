# Generated by Django 4.1.4 on 2023-02-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0003_alter_curd_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curd',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
