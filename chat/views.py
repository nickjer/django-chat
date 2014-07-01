import json
import datetime
from time import strftime
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.http import Http404
from django.utils.cache import patch_cache_control
from django.utils import timezone
from django.utils.timezone import utc

from chat.models import Msg, Author
from chat.forms import MsgForm, ListMsgsForm

class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'

def msgs(request):
    "List all messages in json format starting just after the last msg_id"
    if request.method == 'POST': # Check if form has been submitted
        form = ListMsgsForm(request.POST)
        if form.is_valid(): # All validation rules pass (msg_id is int)
            m_id = form.cleaned_data['msg_id']

            msg_w_auth = Msg.objects.filter(id__gt=m_id).order_by('-id').values('id', 'msg_text', 'author__name')[:10]
    
            msg_list = list(msg_w_auth)
            msg_list.reverse()
            try:
                m_id = msg_list[-1]['id']
            except (IndexError):
                pass
            data = {'msg_id': m_id}
            data['msgs'] = msg_list 
    
            data_json = json.dumps(data, indent=2)
            response = HttpResponse(data_json, content_type='text/json')
            patch_cache_control(response, no_cache=True) #Make sure browser doesn't cache the request
            return response
        else:
            pass
    else:
        pass
    raise Http404

def send(request):
    "Input the user and msg into database then follow up by requesting latest msgs"
    if request.method == 'POST': # Check if form has been submitted
        form = MsgForm(request.POST)
        if form.is_valid(): # All validation rules pass
            author_name = form.cleaned_data['name']
            msg_text = form.cleaned_data['message']

            # Check if user already exists before creating
            auth = Author.objects.get_or_create(name=author_name)[0]
            auth.msg_set.create(msg_text=msg_text)

            return msgs(request) # Display msgs
        else:
            return HttpResponse('', content_type='text/json') # Return nothing
    else:
        raise Http404
