# Generated by Django 4.0.6 on 2022-07-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
