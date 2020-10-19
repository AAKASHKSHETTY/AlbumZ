# Generated by Django 3.0.3 on 2020-03-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0006_camp_boo'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='camp',
            name='boo',
        ),
    ]
