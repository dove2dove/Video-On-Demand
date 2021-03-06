# Generated by Django 2.0.1 on 2018-01-19 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviews', '0002_auto_20180119_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='actors',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='watchlog',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
