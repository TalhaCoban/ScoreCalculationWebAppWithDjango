# Generated by Django 3.0.8 on 2020-08-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogrenci',
            old_name='ogrenci',
            new_name='ogrenci_id',
        ),
    ]