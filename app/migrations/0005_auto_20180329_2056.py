# Generated by Django 2.0.3 on 2018-03-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='resume/'),
        ),
    ]
