# Generated by Django 4.0.6 on 2022-07-25 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_student_active_student_created_student_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='Roll',
            field=models.CharField(max_length=100),
        ),
    ]