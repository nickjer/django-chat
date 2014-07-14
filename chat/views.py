import json
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.http import Http404
from django.utils.cache import patch_cache_control

from chat.models import Msg, Author
from chat.forms import MsgForm, ListMsgsForm

class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'

def msgs(request):
    "List all messages in json format starting just after the last msg_id"
    if request.method == 'GET': # Check if form has been submitted
        form = ListMsgsForm(request.GET)
        if form.is_valid(): # All validation rules pass (msg_id is int)
            m_id = form.cleaned_data['msg_id']

            # Get 10 latest msgs since ``m_id``
            msg_author = Msg.objects.latest_msgs(m_id, 10).values('id', 'msg_text', 'author__name')
            # Convert msgs to list
            msg_list = list(msg_author)

            # Format data into json
            data_json = json.dumps(msg_list, indent=2)

            # Output response as json content
            response = HttpResponse(data_json, content_type='text/json')

            # Make sure browser doesn't cache this request (not sure if needed)
            patch_cache_control(response, no_cache=True)

            return response
        else:
            pass
    else:
        pass
    raise Http404

def send(request):
    "Input the user and msg into database then follow up by requesting latest msgs"
    # Check if user is authenticated
    if request.user.is_authenticated():
        if request.method == 'GET': # Check if form has been submitted
            form = MsgForm(request.GET)
            if form.is_valid(): # All validation rules pass
                author_name = form.cleaned_data['name']
                msg_text = form.cleaned_data['message']

                new_auth = Author.objects.add_author(author_name)
                new_auth.add_msg(msg_text)

    return HttpResponse('') # Return nothing
