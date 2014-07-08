from django.template import Library, Context
from django.template.loader import get_template

from chat.forms import MsgForm

register = Library()

@register.simple_tag
def show_chat(template='chat/chat.html'):
    """
    Displays the chat form as well as live msgs
    using AJAX.

    A user may use a custom template by supplying
    a value for the template_name.
    """

    # Get the msg window form
    form = MsgForm()

    t = get_template(template)

    return t.render( Context({'chat_form': form}) )
