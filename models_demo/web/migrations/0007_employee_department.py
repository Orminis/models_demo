# Generated by Django 4.1.2 on 2022-10-15 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_department_remove_employee_job_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.department'),
        ),
    ]
