# Generated by Django 4.0.6 on 2022-07-26 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_totalcountstudent_alter_student_roll_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalcountstudent',
            name='total_counts',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]