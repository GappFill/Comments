from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comments(MPTTModel):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    autor = models.CharField(max_length=150, verbose_name='Автор комментария')
    text = models.TextField(verbose_name='Текст комментария')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.autor

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

