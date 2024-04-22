from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def discovery_page(request):
    all_blurbs = Blurb.objects.select_related('outlet').all()
    
    context = {
        'blurbs': all_blurbs,
    } # TODO filtering
    
    return render(request, 'discovery.html', context)
