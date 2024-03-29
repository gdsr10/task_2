# Generated by Django 4.2.10 on 2024-02-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='employee_visited',
            new_name='employee_visiting',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='check_in_time',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='check_out_time',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='personal_info',
        ),
        migrations.AlterField(
            model_name='visitor',
            name='status',
            field=models.CharField(choices=[('Waiting for Check in', 'Waiting for Check in'), ('Inside Building', 'Inside Building'), ('Checked Out', 'Checked Out')], max_length=20),
        ),
    ]
