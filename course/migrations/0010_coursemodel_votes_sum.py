# Generated by Django 4.2.11 on 2024-03-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_coursemodel_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='votes_sum',
            field=models.FloatField(default=0),
        ),
    ]
