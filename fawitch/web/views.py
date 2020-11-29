from . import twitchapi, forms, models
from django.shortcuts import render, redirect, reverse,get_list_or_404
from django.contrib import messages

# Create your views here.
def Home(request):
    if request.method == 'POST':
        form_channel = forms.ChannelForm(request.POST)
        if form_channel.is_valid():
            form_channel.save()
            messages.success(request, "استریمر شما با موفقیت ثبت و بعد برسی نمایش داده خواهد شد." )
            return redirect(reverse('index'))

    else:
        try:
            obj = get_list_or_404(models.ChannelModel, show='1')
            streams = twitchapi.get_streams_by_id(twitchapi.get_channels_id([i.channel for i in obj]))
        except Exception:
            models.ChannelModel().channel = 'hajiwarlock'
            models.ChannelModel().show = '1'
            models.ChannelModel().save()
            return redirect(reverse('index'))
        else:
            print(twitchapi.top_viewer(stream=streams, number=3))
            context = {
                'form': forms.ChannelForm(),
                'data': {
                    'viewer' : twitchapi.top_viewer(stream=streams, number=3),
                    'streams': streams,
                }
            }
            return render(request, template_name='index.html', context=context)
