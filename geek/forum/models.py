from django.db import models
import omretuser.models as omretuser_models

# Create your models here.
class Topic(models.Model):
    author = models.ForeignKey(omretuser_models.User)
    subtime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30,null=False)
    content = models.CharField(max_length=5000,null=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    topic = models.ForeignKey('Topic')
    comment_content = models.CharField(max_length=500,null=False)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_user = models.ForeignKey(omretuser_models.User)

    def __str__(self):
        return comment_content
