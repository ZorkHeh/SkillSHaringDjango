from django.shortcuts import render

from .models import Article

def index(request):
    return render(request, "index.html")

def articles(request):
    articles = Article.objects.all()

    context = {'articles': articles}

    return render(request, "articles.html", context)

def article(request, id):
    article = Article.objects.get(pk=1)

    return render(request, "article.html", {'article': article})
