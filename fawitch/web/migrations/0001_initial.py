# Generated by Django 3.1.3 on 2020-11-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(help_text='اسم کانال اسریمر را وارد کنید مثال : AmirPhanThom', max_length=64, unique=True)),
                ('show', models.CharField(choices=[('1', 'نمایش دادن استریمر'), ('0', 'برسی بیشتر')], default='0', max_length=5)),
            ],
        ),
    ]
