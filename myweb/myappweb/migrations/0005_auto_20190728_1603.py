# Generated by Django 2.0 on 2019-07-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappweb', '0004_cjdj_info_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cjdj_info',
            name='cjdate',
            field=models.DateField(),
        ),
    ]