from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    short_content = models.TextField(null=True)
    image = models.ImageField(upload_to='news')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'


