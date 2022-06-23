# Generated by Django 4.0.4 on 2022-06-23 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paquete', '0002_especificacionpaquete_fechainicio_and_more'),
        ('reporte', '0001_initial'),
        ('usuario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('monto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=8, unique=True)),
                ('pagado', models.BooleanField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('pago', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reserva.pago')),
                ('paquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paquete.paquete')),
                ('persona', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.persona')),
                ('reporte', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reporte.reporte')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.reserva')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
