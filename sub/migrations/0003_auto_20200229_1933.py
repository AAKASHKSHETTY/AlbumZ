# Generated by Django 3.0.3 on 2020-02-29 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0002_auto_20200229_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adopt',
            old_name='picture',
            new_name='pictures',
        ),
    ]