# Generated by Django 3.0.6 on 2020-05-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_NOTES', '0003_auto_20200527_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnscl',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='cnscl',
            name='question',
            field=models.TextField(),
        ),
    ]