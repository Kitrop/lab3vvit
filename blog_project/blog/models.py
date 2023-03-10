# blog/models.py
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return "%s: %s" % (self.author.username, self.title)

    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
