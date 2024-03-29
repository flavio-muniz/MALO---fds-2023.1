# Generated by Django 4.2 on 2023-05-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Malo_App', '0019_rename_orders_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garcom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('cargo', models.CharField(max_length=120, verbose_name='Cargo')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Salário')),
                ('login', models.CharField(max_length=120, verbose_name='Login')),
            ],
        ),
    ]
