# Generated by Django 5.1.5 on 2025-01-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('patient', 'Patient'), ('nurse', 'Nurse')], default='patient', max_length=50),
        ),
    ]
