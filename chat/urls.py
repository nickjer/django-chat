from django.conf.urls import patterns, url

from chat import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^msgs/$', views.msgs, name='msgs'),
    url(r'^send/$', views.send, name='send'),
)
