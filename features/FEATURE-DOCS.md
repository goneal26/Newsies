# "features" app
The 'features' app consists of the templates, views, and models for defining end-user interactions with the main features of the app.

Templates are defined in `features/templates/`.

The class/implementation for *fetching RSS feeds to populate blurbs* is written/documented in `features/rss.py`.

---

## Views

### outlets_page(*request*)
Renders the outlets page displaying all outlets and whether the current user follows each outlet.

- **Method:** GET
- **Decorator:** `@login_required`
- **Template:** `outlets.html`

#### Context:
- **outlets**: QuerySet of all outlets annotated with a boolean indicating if the current user follows each outlet.

---

### follow(*request, pk*)
Handles the follow/unfollow action for a specific outlet.

- **Method:** POST
- **Decorator:** `@login_required`, `@require_POST`
- **Parameters:**
  - **pk**: Primary key of the outlet to follow/unfollow.
  
#### Returns:
- Redirects to the URL specified in the request POST data.

---

### podcasts_page(*request*)
Renders the podcasts page displaying all available podcasts.

- **Method:** GET
- **Decorator:** `@login_required`
- **Template:** `podcasts.html`

#### Context:
- **podcasts**: QuerySet of all podcasts ordered by name.

---

### discovery_page(*request*)
Renders the discovery page with blurbs filtered by search queries or tags.

- **Method:** GET, POST (for search/filtering)
- **Decorator:** `@login_required`
- **Template:** `discovery.html`

#### Context:
- **blurbs**: QuerySet of blurbs annotated with vote counts and filtered by search queries or tags.
- **filter_text**: Text used for filtering blurbs.

---

### home_page(*request*)
Renders the home page displaying blurbs from followed outlets.

- **Method:** GET
- **Decorator:** `@login_required`
- **Template:** `home.html`

#### Context:
- **blurbs**: QuerySet of blurbs from followed outlets ordered by date.

---

### vote(*request, pk*)
Handles upvoting or downvoting a blurb.

- **Method:** POST
- **Decorator:** `@login_required`, `@require_POST`
- **Parameters:**
  - **pk**: Primary key of the blurb to vote on.
  
#### Returns:
- Redirects to the URL specified in the request POST data.

---

### post_comment(*request, pk*)
Handles posting a comment on a blurb.

- **Method:** POST
- **Decorator:** `@login_required`, `@require_POST`
- **Parameters:**
  - **pk**: Primary key of the blurb to comment on.
  
#### Returns:
- Redirects to the URL specified in the request POST data.

---

### delete_comment(*request, pk*)
Handles deleting a comment on a blurb.

- **Method:** POST
- **Decorator:** `@login_required`, `@require_POST`
- **Parameters:**
  - **pk**: Primary key of the comment to delete.
  
#### Returns:
- Redirects to the URL specified in the request POST data.

---

### vote_comment(*request, pk*)
Handles upvoting or downvoting a comment.

- **Method:** POST
- **Decorator:** `@login_required`, `@require_POST`
- **Parameters:**
  - **pk**: Primary key of the comment to vote on.
  
#### Returns:
- Redirects to the URL specified in the request POST data.

---

### read_article(*request*)
Handles counting when a user clicks to read an article for reading badges.

- **Method:** POST
- **Decorator:** `@login_required`, `@require_POST`
  
#### Returns:
- Redirects to the URL specified in the request POST data after incrementing the articles read count for the user's profile.

---

## Models

### Tag
Simple model representing a tag for categorization.

#### Fields:
- **name**: Name of the tag.
  - *Max Length*: 50 characters (unique)

#### Methods:
- **__str__()**:
  Returns a string representation of the tag prefixed with `#`.

---

### Outlet
Model representing a news outlet.

#### Fields:
- **rss_url**: URL for the outlet's RSS feed.
- **page_url**: URL of the outlet's page (default: empty string).
- **name**: Name of the outlet.
  - *Max Length*: 255 characters
- **logo**: ImageField for the outlet's logo.
  - *Default*: `'images/default.png'`, stored in `outlet_logos/`
- **followers**: Many-to-many relationship with `User` model for followers.

#### Methods:
- **__str__()**:
  Returns a string representation of the outlet.

#### Custom Save Method:
Overrides the default `save()` method to resize and save the outlet's logo.

---

### Blurb
Model representing a news blurb.

#### Fields:
- **title**: Title of the blurb.
  - *Max Length*: 255 characters
- **description**: Description/content of the blurb.
- **outlet**: ForeignKey to the `Outlet` model.
- **link**: URL link associated with the blurb.
  - *Max Length*: 255 characters
- **date**: DateTimeField for blurb publishing date/time.
- **upvotes**: Many-to-many relationship with `User` model for upvotes.
- **downvotes**: Many-to-many relationship with `User` model for downvotes.
- **tags**: Many-to-many relationship with `Tag` model for categorization.

#### Methods:
- **__str__()**:
  Returns a string representation of the blurb.

#### Custom Class Method:
- **create(cls, blurb_content, source)**:
  Creates a new `Blurb` object using a dictionary of blurb content.

---

### Comment
Model representing a user comment on a blurb.

#### Fields:
- **author**: ForeignKey to the `User` model for the comment author.
- **blurb**: ForeignKey to the `Blurb` model for the associated blurb.
- **text**: Text content of the comment.

#### Methods:
- **__str__()**:
  Returns a string representation of the comment.

#### Additional Methods:
- **net_votes()**:
  Calculates the net votes (upvotes minus downvotes) for the comment.

---

### Podcast
Model representing a podcast.

#### Fields:
- **url**: URL of the podcast.
- **name**: Name of the podcast.
  - *Max Length*: 255 characters
- **author**: Author of the podcast.
  - *Max Length*: 255 characters
- **logo**: ImageField for the podcast's logo, stored in `podcast_logos/`

#### Methods:
- **__str__()**:
  Returns a string representation of the podcast.

