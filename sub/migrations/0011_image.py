# Generated by Django 3.0.3 on 2020-03-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0010_auto_20200309_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='pictures', verbose_name='')),
            ],
        ),
    ]