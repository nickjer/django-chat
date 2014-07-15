from django.db import models
from django.contrib.auth.models import User

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

class Msg(models.Model):
    author = models.ForeignKey(User)
    msg_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)

    objects = MsgManager()

    def __str__(self):
        return self.msg_text
