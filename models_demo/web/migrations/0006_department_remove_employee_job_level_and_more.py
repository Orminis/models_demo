# Generated by Django 4.1.2 on 2022-10-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_employee_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='job_level',
        ),
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], max_length=7, verbose_name='Seniority Level'),
        ),
    ]