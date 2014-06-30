django-chat
===========

A terrible chat application to help me better explore the django framework.

## Key features

* AJAX support for realtime updates
* Nothing else so far, since this is an educational tool for myself...

## Installation

In order to install copy over the "chat" directory from GitHub.

Add `chat` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'chat',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^your-url/$', include('chat.urls', namespace="chat")),
        ...
    )

Run `python manage.py migrate` to create the chat models.

Start the development server and visit http://127.0.0.1:8000/chat/ to participate in the chat.

## Versions

This is the only version.

- all versions require Python3
- all versions require Django1.6 (not tested below)
