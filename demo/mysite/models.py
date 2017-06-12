from django.db import models
from django.contrib.auth.models import User

# Create article table in db
class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

# Create reply table in db
class Reply(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    reply_content = models.CharField(max_length=250)
    replay_pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.reply_content