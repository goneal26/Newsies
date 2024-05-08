from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from users.models import Profile
from django.http import JsonResponse
from django.db.models import Count, BooleanField, Case, When, Q
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
    ).order_by('-vote_count', '-date').all() # should filter them by vote count

    filter_text = ""

    # if searching
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            filter_text = query
            if query[0] == '#' and len(query) > 1: # if searching for tag
                tagname = query[1:].strip()
                all_blurbs = all_blurbs.filter(tags__name=tagname)
            else: # searching for keyword
                all_blurbs = all_blurbs.filter(
                    Q(title__icontains=query) | Q(description__icontains=query)
                )
    
    context = {
        'blurbs': all_blurbs,
        'filter_text': filter_text
    }
    
    return render(request, 'discovery.html', context)

@login_required
def home_page(request):
    followed_blurbs = Blurb.objects.filter(outlet__followers=request.user).annotate(
        vote_count =  Count('upvotes') - Count('downvotes')
    ).order_by('-date').all() # should filter them by vote count

    context = {
        'blurbs': followed_blurbs,
    }

    return render(request, 'home.html', context)


@login_required
@require_POST
def vote(request, pk):
    url = request.POST.get('next', '/')
    blurb = get_object_or_404(Blurb, pk=pk)

    if 'upvote' in request.POST:
        if request.user in blurb.upvotes.all():
            blurb.upvotes.remove(request.user)
        else:
            if request.user in blurb.downvotes.all():
                blurb.downvotes.remove(request.user)
            blurb.upvotes.add(request.user)
    elif 'downvote' in request.POST:
        if request.user in blurb.downvotes.all():
            blurb.downvotes.remove(request.user)
        else:
            if request.user in blurb.upvotes.all():
                blurb.upvotes.remove(request.user)
            blurb.downvotes.add(request.user)
    
    return redirect(url)

@login_required
@require_POST
def post_comment(request, pk):
    url = request.POST.get('next', '/')
    text = request.POST.get('input-text')
    user = request.user
    blurb = get_object_or_404(Blurb, pk=pk)

    if text: # don't post empty comments
        # parsing comment for tags
        arr = text.split(' ')
        for word in arr:
            if len(word) > 1 and word[0] == '#':
                tagname = word[1:]
                if Tag.objects.filter(name=tagname): # tag already exists, but no relationship with this blurb
                    newtag = get_object_or_404(Tag, name=tagname)
                    if newtag not in blurb.tags.all(): # only add new relationship if there isnt one already
                        blurb.tags.add(newtag)
                else: # new tag being created
                    newtag = Tag(name=word[1:])
                    newtag.save()
                    blurb.tags.add(newtag)

        # saving comment
        comment = Comment(author=user, blurb=blurb, text=text)
        comment.save()

    return redirect(url)

@login_required
@require_POST
def delete_comment(request, pk):
    # simple enough, I'll go back and add editing later (time permitting)
    url = request.POST.get('next', '/')
    comment = Comment.objects.get(pk=pk)

    # delete all tags in comment
    text = comment.text
    arr = text.split(' ')
    for word in arr:
        if len(word) > 1 and word[0] == '#':
            tagname = word[1:]
            tag = get_object_or_404(Tag, name=tagname)
            comment.blurb.tags.remove(tag)

    # delete comment
    comment.delete()

    return redirect(url)

@login_required
@require_POST
def vote_comment(request, pk):
    url = request.POST.get('next', '/')
    comment = get_object_or_404(Comment, pk=pk)

    if 'upvote' in request.POST:
        if request.user in comment.upvotes.all():
            comment.upvotes.remove(request.user)
        else:
            if request.user in comment.downvotes.all():
                comment.downvotes.remove(request.user)
            comment.upvotes.add(request.user)
    elif 'downvote' in request.POST:
        if request.user in comment.downvotes.all():
            comment.downvotes.remove(request.user)
        else:
            if request.user in comment.upvotes.all():
                comment.upvotes.remove(request.user)
            comment.downvotes.add(request.user)

    return redirect(url)

@login_required
@require_POST
def read_article(request): # for counting a user clicks a "read more" link for reading badges
    url = request.POST.get('next', '/')
    profile = request.user.profile

    profile.articles_read += 1 # increment articles read
    profile.save()

    return redirect(url)