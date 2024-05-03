from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from django.db.models import Count, BooleanField, Case, When
from django.views.decorators.http import require_POST

@login_required
def outlets_page(request):
    all_outlets = Outlet.objects.order_by('-name').all().annotate(
        # annotate with True if the current user follows this outlet
        has_follower = Case(
            When(followers=request.user, then=True),
            default=False,
            output_field=BooleanField()
        )
    )

    context = {
        'outlets': all_outlets,
    }

    return render(request, 'outlets.html', context)

@login_required
@require_POST
def follow(request, pk):
    url = request.POST.get('next', '/')
    outlet = get_object_or_404(Outlet, pk=pk)

    if request.user in outlet.followers.all():
        outlet.followers.remove(request.user)
        print("Unfollowed")
    else:
        outlet.followers.add(request.user)

    return redirect(url)

@login_required
def podcasts_page(request):
    all_podcasts = Podcast.objects.order_by('-name').all()

    context = {
        'podcasts': all_podcasts
    }

    return render(request, 'podcasts.html', context)

@login_required
def discovery_page(request):
    all_blurbs = Blurb.objects.select_related('outlet').annotate(
        vote_count =  Count('upvotes') - Count('downvotes')
    ).order_by('-vote_count').all() # should filter them by vote count
    
    context = {
        'blurbs': all_blurbs,
    }
    
    return render(request, 'discovery.html', context)

@login_required
def home_page(request):
    followed_blurbs = Blurb.objects.filter(outlet__followers=request.user)

    context = {
        'blurbs': followed_blurbs,
    }

    return render(request, 'home.html', context)

# TODO maybe refactor these to be more like the follow view- separate POST api urls
# using HTML form actions
@login_required
def upvote(request, pk):
    if request.method == "POST":
        blurb = get_object_or_404(Blurb, pk=pk)
        if request.user in blurb.downvotes.all():
            blurb.downvotes.remove(request.user)
        blurb.upvotes.add(request.user)
        return JsonResponse({
            'success': True, 
            'upvotes': blurb.upvotes.count(), 
            'downvotes': blurb.downvotes.count()
        })
    return JsonResponse({'success': False})

@login_required
def downvote(request, pk):
    if request.method == "POST":
        blurb = get_object_or_404(Blurb, pk=pk)
        if request.user in blurb.upvotes.all():
            blurb.upvotes.remove(request.user)
        blurb.downvotes.add(request.user)
        return JsonResponse({
            'success': True, 
            'upvotes': blurb.upvotes.count(), 
            'downvotes': blurb.downvotes.count()
        })
    return JsonResponse({'success': False})