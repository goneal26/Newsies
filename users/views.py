from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

def register(request):
    """
    Handle user registration.

    - If the request method is POST, attempt to create a new user account using
      the data provided in the form.
    - Validate the form data. If valid, save the new user and redirect to the 
      login page with a success message.
    - If the request method is not POST (i.e., GET), display a blank 
      registration form.

    Args:
        request: HttpRequest object containing metadata about the request.

    Returns:
        HttpResponse object with the registration form rendered in the 
        register HTML template.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form}) 
    

@login_required
def current_user_profile(request):
    has_badge = request.user.profile.articles_read > 10 # 10 articles to get badge for now

    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            print(request.POST.get('image'))
            user_form.save()
            profile_form.save()

        messages.success(request, 'Your account has been updated!')
        return redirect('profile') # redirect back to pfp to display updates
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'has_badge': has_badge,
    }

    return render(request, 'profile.html', context)