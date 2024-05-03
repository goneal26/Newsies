"""
URL configuration for newsies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
# ^ shouldn't need "include" if urls defined only in here
from features import views as feature_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static # for media folder
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # user authentication urls
    path('register/', user_views.register, name='register'),
    path(
        'login/', 
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path( # log out
        'logout/', 
        auth_views.LogoutView.as_view(next_page='login'), 
        name='logout'
    ),

    # current-user profile page
    path('profile/', user_views.current_user_profile, name='profile'),

    # outlet following
    path('follow/<int:pk>/', feature_views.follow, name='follow'),

    # partnered outlets page
    path('outlets/', feature_views.outlets_page, name="outlets"),

    # podcasts page
    path('podcasts/', feature_views.podcasts_page, name="podcasts"),

    # home page
    path('home/', feature_views.home_page, name="home"),

    # discovery page urls
    path('discover/', feature_views.discovery_page, name="discover"),
    path('discover/<int:pk>/upvote/', feature_views.upvote, name='upvote'),
    path('discover/<int:pk>/downvote/', feature_views.downvote, name='downvote'),

]

# TODO: revisit before deployment (shouldn't deploy with settings.DEBUG)
# see https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/
if settings.DEBUG: # access to media folder VVV
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
