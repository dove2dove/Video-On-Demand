# Generated by Django 2.0.1 on 2018-01-25 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviews', '0008_auto_20180125_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='mediumPicture',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
