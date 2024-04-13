from django.shortcuts import render
from .models import *

# Create your views here.

def discovery_page(request):
    all_blurbs = Blurb.objects.select_related('outlet').all()

    
    context = {
        'blurbs': all_blurbs,
    }

    return render(request, 'discovery.html', context)
