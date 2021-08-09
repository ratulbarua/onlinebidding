# Generated by Django 3.1.1 on 2020-10-06 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionItem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='title',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='photo',
            new_name='seller_photo',
        ),
        migrations.AlterField(
            model_name='lot',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='year_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 16, 51, 9, 989242)),
        ),
    ]