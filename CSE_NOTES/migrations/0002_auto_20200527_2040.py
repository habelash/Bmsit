# Generated by Django 3.0.6 on 2020-05-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_NOTES', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnscl',
            name='qno',
            field=models.IntegerField(),
        ),
    ]
