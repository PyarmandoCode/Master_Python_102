# Generated by Django 5.0 on 2024-08-17 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empleados')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('empleados', models.ManyToManyField(to='core.empleados')),
            ],
        ),
        migrations.CreateModel(
            name='Pasaporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasaporte_numero', models.CharField(max_length=50)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.empleados')),
            ],
        ),
    ]
