# Generated by Django 3.2.12 on 2023-04-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Malo_App', '0012_merge_20230416_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='exp_date',
            field=models.DateField(verbose_name='Data de validade'),
        ),
    ]
