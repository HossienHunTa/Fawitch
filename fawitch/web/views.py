from django.shortcuts import get_list_or_404, render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from distutils.util import strtobool
from html import escape
from . import twitchapi, models

# Create your views here.
def Home(request):
    if request.method == 'POST':
        if not request.POST.get('channel') == '':
            try:
                obj = models.ChannelModel()
                obj.channel = escape(str(request.POST.get('channel')).lower())
                obj.save()
            except:
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
    else:
        obj = get_list_or_404(models.ChannelModel,show='1')
        try:
            streams = twitchapi.get_streams_by_id(twitchapi.get_channels_id([i.channel for i in obj]))
        except Exception as e:
            streams = {}   
        context = {
            'data': {
                'viewer' : twitchapi.three_top_viewer(stream=streams),
                'streams': streams,
            }
        }
        return render(request, template_name='index.html', context=context)
