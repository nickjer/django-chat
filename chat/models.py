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
        new_auth = Author.objects.get_or_create(name=author_name)[0]

        return new_auth

class Author(models.Model):
    name = models.CharField(max_length=25)

    objects = AuthManager()

    def __str__(self):
        return self.name

    def add_msg(self, msg_text):
        "Add msg for this author."
        self.msg_set.create(msg_text=msg_text)

class Msg(models.Model):
    author = models.ForeignKey(Author)
    msg_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)

    def __str__(self):
        return self.msg_text
