from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# main resource for all auth stuff is from our last project
# (authentication for Newsies should behave the same as how NuPath was supposed
# to, so why change anything?)

class ProfileUpdateForm(forms.ModelForm):
	"""
    A form for updating the user's profile, specifically the profile image.

    Meta:
        model (Profile): The custom Profile model related to the User model.
        fields (list): Defines the 'image' field for the form, allowing users to update their profile image.
    """
	class Meta:
		model = Profile
		fields = ['image']

class UserRegisterForm(UserCreationForm):
    """
    A form for creating new users. Inherits from Django's UserCreationForm and 
    adds an email field.

    Attributes:
        email (EmailField): An additional field for user email. Required for 
        user registration.

    Meta:
        model (User): The Django default User model used for creating the form 
                      fields.
        fields (list): Specifies the fields to be used in the form. Includes 
                       username, email, password (password), and 
                       password_confirm (password confirmation).
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    """
    A form for updating user information. Specifically designed for updating 
    username and email.

    Attributes:
        email (EmailField): Field for updating the user's email. Required for 
                            the form.

    Meta:
        model (User): The Django User model to which the form is tied.
        fields (list): Fields included in the form, allowing the user to update 
                       their username and email.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']