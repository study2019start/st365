# Generated by Django 2.0 on 2019-06-15 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappweb', '0003_cjdj_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='cjdj_info',
            name='area',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
