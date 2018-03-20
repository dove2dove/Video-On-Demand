# Generated by Django 2.0.1 on 2018-02-03 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviews', '0012_genres_categorytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='categoryType',
            field=models.CharField(blank=True, choices=[('TV', 'Tv'), ('MV', 'Movies'), ('BT', 'Both')], default='BT', max_length=25, null=True),
        ),
    ]