# Generated by Django 3.1.5 on 2021-02-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0004_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
