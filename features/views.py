from django.shortcuts import render
from .models import Article  # Assuming you have an Article model

# Create your views here.

def newsfeed(request):
    articles = Article.objects.all()  # Fetch all articles from the database
    return render(request, 'newsfeed.html', {'articles': articles})
