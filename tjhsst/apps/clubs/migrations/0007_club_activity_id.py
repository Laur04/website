# Generated by Django 2.2.6 on 2019-10-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_auto_20190509_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='activity_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
