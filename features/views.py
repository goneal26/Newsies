from django.shortcuts import render
from .models import Article  # Assuming you have an Article model
from .models import FollowedPage # Assuming you have a model for user-followed pages

# Create your views here.

def newsfeed(request):
    articles = Article.objects.all()  # Fetch all articles from the database
    return render(request, 'newsfeed.html', {'articles': articles})

def followed_pages(request):
    # Fetch the pages the user follows (you'll need to implement this logic)
    followed_pages = FollowedPage.objects.filter(user=request.user)
    return render(request, 'followed_pages.html', {'followed_pages': followed_pages})
