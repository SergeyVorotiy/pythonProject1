# Generated by Django 4.1.1 on 2022-09-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_filewordcounts_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='filewordcounts',
            name='file',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]
