# Generated by Django 2.1.7 on 2019-05-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0006_merge_20190509_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='description',
            field=models.CharField(default='This lab page has not yet been filled out.', max_length=5000),
        ),
    ]
