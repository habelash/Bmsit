# Generated by Django 3.0.6 on 2020-05-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_NOTES', '0002_auto_20200527_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnscl',
            name='answer',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='cnscl',
            name='qno',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cnscl',
            name='question',
            field=models.CharField(max_length=1000),
        ),
    ]