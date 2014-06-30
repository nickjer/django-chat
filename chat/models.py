from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Msg(models.Model):
    author = models.ForeignKey(Author)
    msg_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    def __str__(self):
        return self.msg_text
