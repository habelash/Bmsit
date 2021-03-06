# Generated by Django 3.0.6 on 2020-05-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_NOTES', '0004_auto_20200527_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='cg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.PositiveIntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='opr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.PositiveIntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='os',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.PositiveIntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pyth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.PositiveIntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.PositiveIntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
