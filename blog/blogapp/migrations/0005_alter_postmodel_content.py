# Generated by Django 3.2.6 on 2021-08-11 13:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_alter_postmodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
