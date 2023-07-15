# Generated by Django 4.2.3 on 2023-07-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('content', models.CharField(max_length=1000000)),
                ('word_count', models.IntegerField()),
                ('char_count', models.IntegerField()),
                ('creation_date', models.CharField(max_length=50)),
            ],
        ),
    ]
