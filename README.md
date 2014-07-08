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

## Usage

This Chat app provides a simple template tag and override-able template that does the work of integrating the chat CSS, JavaScript, and HTML into your site.

To place the chat widget in a template, simply insert the following within it:

    {% load chat %}
    {% show_chat %}

## Customization

This chat app is designed to be customizable.

The chat template tag optionally takes the argument the name of the template to load and override the default template:

    {% load chat %}
    {% show_chat 'your_template.html' %}

A custom template can extend from the master chat template chat/chat.html. There are several blocks which may be overridden for the purpose of customization. For instance, one could got about adding a more up to date JQuery library or plugging in a new CSS layout:

    # your_template.html
    {% extends 'chat/chat.html' %}
    
    {% block jquery_js %}
        <script src="{{ STATIC URL }}/js/my.newer.jquery.js"></script>
    {% endblock %}
    
    {% block chat_css %}
        <link href="{{ STATIC URL }}/css/cooler.theme.css" type="text/css" media="all" rel="stylesheet" />
    {% endblock %}

or you can simply replace the static files themselves.

## Versions

This is the only version.

- all versions require Python3
- all versions require Django1.6 (not tested below)
