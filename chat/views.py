import json
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.utils.cache import patch_cache_control

from chat.models import Msg, Author

class IndexView(generic.TemplateView):
    template_name = 'chat/index.html'

def msgs(request):
    try:
        m_id = int(request.POST['msg_id'])
    except (KeyError):
        m_id = 0;

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

def send(request):
    # Input the user and msg into database
    try:
        author_name = request.POST['name']
        msg_text = request.POST['message']
    except (KeyError):
        return HttpResponse('', content_type='text/json')

    # Check if user already exists before creating
    auth = Author.objects.get_or_create(name=author_name)[0]
    auth.msg_set.create(msg_text=msg_text)

    # Display msgs now
    response = msgs(request)
    return response
