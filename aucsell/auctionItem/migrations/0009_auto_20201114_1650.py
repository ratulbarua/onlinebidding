# Generated by Django 3.1.3 on 2020-11-14 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0008_auto_20201114_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 14, 16, 50, 44, 309894)),
        ),
    ]
