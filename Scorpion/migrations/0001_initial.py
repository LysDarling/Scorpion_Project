# Generated by Django 4.2.3 on 2023-07-04 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('duracion', models.PositiveIntegerField(verbose_name='Minutos')),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scorpion.cliente')),
                ('servicio', models.ManyToManyField(to='Scorpion.servicio')),
            ],
            options={
                'verbose_name_plural': 'Citas',
            },
        ),
    ]