from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snippet(models.Model):
    text = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    UserInfo = models.ForeignKey(User, on_delete=models.CASCADE)
    TagInfo = models.ForeignKey('app.Tag', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'

    def __str__(self):
        return "{}".format(self.TagInfo.title)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return "/api/overview/snippet/{}".format(self.id)