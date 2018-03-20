# Generated by Django 2.0.1 on 2018-02-03 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviews', '0011_genres_displayphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='genres',
            name='categoryType',
            field=models.CharField(blank=True, choices=[('FM', 'Tv'), ('TR', 'Movies'), ('SM', 'Both')], default='SM', max_length=25, null=True),
        ),
    ]