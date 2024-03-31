# Generated by Django 4.2.11 on 2024-03-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialtrialmodel',
            name='situation',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='financialtrialmodel',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='financialtrialmodel',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='financialtrialmodel',
            name='level',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='financialtrialmodel',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='financialtrialmodel',
            name='question',
            field=models.CharField(max_length=500, null=True),
        ),
    ]