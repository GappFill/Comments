from django.shortcuts import render, get_object_or_404

from .models import Articles, Comments
from .forms import CommentFrom

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, template_name='notes/index.html',context=context)


def getArticle(request, article_id):  # Комментарии должны выводиться тут
    article = Articles.objects.filter(id=article_id)  # Комеентарии надо выгрузить

    if request.method == 'POST':
        comment_form = CommentFrom(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article_id = article_id
            new_comment.save()

    comment_form = CommentFrom()
    comments = Comments.objects.filter(article_id=article_id)
    context = {
        'article': article,
        'form': comment_form,
        'comments': comments,
    }
    return render(request, template_name='notes/article.html', context=context)