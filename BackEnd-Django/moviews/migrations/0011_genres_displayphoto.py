# Generated by Django 2.0.1 on 2018-02-03 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviews', '0010_auto_20180203_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='genres',
            name='displayphoto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
