import html
from django.db import models

class AuthManager(models.Manager):
    """
    Custom manager for the ``Author`` model.

    The methods defined here provide shortcuts
    to author creation...
    """
    def add_author(self, author_name):
        """
        Check if author exists before adding them
        Then return this author
        """
        author_name_esc = html.escape(author_name) # Escape HTML code in author name
        new_auth = Author.objects.get_or_create(name=author_name_esc)[0]

        return new_auth

class MsgManager(models.Manager):
    """
    Custom manager for the ``Msg`` model.

    The methods defined here provide shortcuts
    to get latest msgs...
    """
    def latest_msgs(self, msg_id=0, num=10):
        """
        Get ``num`` latest msgs using id's greater
        than ``msg_id``.
        """
        msg_query = Msg.objects.filter(id__gt=msg_id).order_by('-id')[:num]

        return msg_query

class Author(models.Model):
    name = models.CharField(max_length=25)

    objects = AuthManager()

    def __str__(self):
        return self.name

    def add_msg(self, msg_text):
        "Add msg for this author."
        msg_text_esc = html.escape(msg_text) # Escape HTML code in msg
        self.msg_set.create(msg_text=msg_text_esc)

class Msg(models.Model):
    author = models.ForeignKey(Author)
    msg_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)

    objects = MsgManager()

    def __str__(self):
        return self.msg_text
