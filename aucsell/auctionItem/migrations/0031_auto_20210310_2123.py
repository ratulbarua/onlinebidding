# Generated by Django 3.1.5 on 2021-03-10 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0030_auto_20201127_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 21, 23, 26, 680430)),
        ),
    ]
