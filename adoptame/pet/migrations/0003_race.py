# Generated by Django 4.2.6 on 2023-11-08 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_alter_specie_options_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Raza')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.specie')),
            ],
        ),
    ]
