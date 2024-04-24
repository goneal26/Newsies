from django.shortcuts import render
from .models import Article  # Assuming you have an Article model
from .models import FollowedPage # Assuming you have a model for user-followed pages
from .models import NewsOutlet # Assuming you have a model for news outlets

# Create your views here.

def newsfeed(request):
    articles = Article.objects.all()  # Fetch all articles from the database
    return render(request, 'newsfeed.html', {'articles': articles})

def followed_pages(request):
    # Fetch the pages the user follows (you'll need to implement this logic)
    followed_pages = FollowedPage.objects.filter(user=request.user)
    return render(request, 'followed_pages.html', {'followed_pages': followed_pages})

def news_outlets(request):
    """
    View function to render the news outlets page.
    Retrieves a list of news outlets from the database and passes it to the template.
    """
    news_outlets = NewsOutlet.objects.all()
    context = {'news_outlets': news_outlets}
    return render(request, 'Newsies/features/templates/outlets.html', context)
