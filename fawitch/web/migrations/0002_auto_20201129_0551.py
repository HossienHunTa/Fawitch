# Generated by Django 3.1.3 on 2020-11-29 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelmodel',
            name='show',
            field=models.CharField(choices=[('1', 'نمایش دادن استریمر'), ('0', 'برسی بیشتر')], default='0', max_length=1),
        ),
    ]
