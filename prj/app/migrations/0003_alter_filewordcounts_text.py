# Generated by Django 4.1.1 on 2022-09-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_filewordcounts_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filewordcounts',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
