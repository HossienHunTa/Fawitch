from django import forms
from django.contrib import messages
from .models import ChannelModel


class ChannelForm(forms.ModelForm):
    channel = forms.CharField(min_length=3, required=True, help_text='اسم کانال اسریمر را وارد کنید مثال : AmirPhanThom',)
    class Meta:
        model = ChannelModel
        fields = ['channel']
    
    def clean_channel(self):
        channel = self.cleaned_data.get("channel")
        if ChannelModel.objects.filter(channel=channel).exists():
            raise 'Error To Submit streamer!!'
        return channel