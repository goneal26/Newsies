# "users" app
The 'users' app consists of the templates, views, and models for user authentication and profiles.

Templates are defined in `users/templates/`.

When it comes to developer contributions, Alexander wrote the frontend HTML/CSS for this app while Tre wrote the views and models (`views.py` and `models.py`).

## Views

### register(*request*)
Handles user registration form submissions and rendering of the registration page.

- **Method:** POST (for form submission), GET (for rendering the form)
- **Decorator:** None
- **Template:** `users/register.html`

This view creates a new user account if the form data is valid. Upon successful registration, the user is redirected to the login page.

---

### current_user_profile(*request*)
Displays the profile page of the currently logged-in user and handles profile updates.

- **Method:** GET (for rendering), POST (for profile updates)
- **Decorator:** `@login_required`
- **Template:** `users/profile.html`, `users/edit-profile.html`


## Models

### Profile
The Django model representing a user profile.

#### Fields:
- **user**: One-to-one relationship with a Django `User` object.
- **image**: Profile image stored in `media/pfps/` directory.
  - *Default*: `'images/default.png'`
- **articles_read**: Counter tracking the number of news articles read by the user.
  - *Default*: `0`

#### Methods:
- **has_badge()**:
  Determines if the user qualifies for a badge based on the number of articles read.
  - **Returns**: `True` if `articles_read` is greater than 10; otherwise `False`.

#### Custom Save Method:
Overrides the default `save()` method to handle image resizing.

This method automatically resizes profile images to fit within a 300x300 box while maintaining the aspect ratio.

##### Parameters:
- `*args`: Variable-length argument list.
- `**kwargs`: Arbitrary keyword arguments.

The image is processed during the save operation to ensure it meets the size constraints specified.

