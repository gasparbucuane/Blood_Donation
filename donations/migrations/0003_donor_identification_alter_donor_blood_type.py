# Generated by Django 5.0.7 on 2024-07-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_alter_donor_blood_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='identification',
            field=models.TextField(default='default_value', max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='blood_type',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
    ]
