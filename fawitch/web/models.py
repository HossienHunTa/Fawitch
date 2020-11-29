from django.db import models

# Create your models here.
class ChannelModel(models.Model):
    SHOW_CHOICES = (
        ('1','نمایش دادن استریمر'),
        ('0','برسی بیشتر'),
    )
    channel = models.CharField(unique=True,max_length=64,help_text='اسم کانال اسریمر را وارد کنید مثال : AmirPhanThom',)
    show = models.CharField(choices=SHOW_CHOICES, max_length=1, default='0')


