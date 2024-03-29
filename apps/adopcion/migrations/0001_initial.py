# Generated by Django 3.0.5 on 2020-04-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('telefono', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.TextField(max_length=50)),
            ],
        ),
    ]
