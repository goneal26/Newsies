# Newsies
Team Churro Final Project
(Alexander and Tre)

## About Newsies
Newsies is a news-feed app implemented in Django, where the app allows users to see summary information (in the form of "Blurbs") on the latest news articles from a number of news outlets, updated daily via RSS feed fetching. 
Users can upvote and downvote on these "blurbs" to boost their popularity in the app's main feed, as well as follow news outlets they like to have them appear in their "home" feed.
Users can also post comments underneath these "blurbs," and if they click the link to read the external news article, they work their way towards a "reading" badge that other users on the platform can see, rewarding users for interacting with the news.
Users can also post "#tags" in the comments underneath blurbs, allowing them to filter their feed by tag by searching for that tag in the search bar.

You can visit the currently deployed build [here](https://goneal26.pythonanywhere.com/).

## Team Churro
This project was developed by Team Churro- Alexander and Tre. 

Tre was tasked with implementing the app's RSS fetching to generate "blurbs", user authentication and profiles, database models for storing and displaying partnered news outlets on the "outlets" page, implementing the system for users to post and filter by "#tags", implementing the system for user upvoting and downvoting, and project deployment.

Alexander was tasked with developing frontend templates for each of the pages of the project, implementing the system for users to follow news outlets for them to be displayed on their home feed, and user commenting.

Specific contributions are made more clear by comments in the codebase.

## Installation Instructions
__Note__: The "main" branch of this project is the main development branch, for modifying and running the app/project locally. The "deployed" branch is slightly different, as it has some minor changes so that in can specifically run on PythonAnywhere. This branch has features that work on PythonAnywhere that may not work when running the project locally. These installation instructions are for installing and developing on the "main" branch.

1. Prerequisites 

Ensure that you have the following installed on your system:
 - Python 3.11.5 (Python 3.10 and later works as well)
 - `pip`, Python's package manager
 - `git`, for cloning the repository

2. Clone the repository

Clone the GitHub repository with this command:

```
git clone https://github.com/goneal26/Newsies.git
```

Now you should navigate to the repository in a folder called "Newsies".

3. Set up a virtual environment (optional but recommended)

Inside the repository folder, set up a virtual environment with the following command:

```
python3 -m venv venv
```

Now, activate the virtual environment:
 - On Windows:
 	```
 	venv\Scripts\activate
 	```
 - On macOS/Linux:
 	```
 	source venv/bin/activate
 	```

4. Install dependences

Ensure you are in the repository folder ("Newsies", where "requirements.txt" is located) and install the required Python packages:
```
pip install -r requirements.txt
```

5. Set Up Django App

Run database migrations:
```
python manage.py migrate
```

6. Create a superuser (admin)

Optionally, create a superuser to access the Django admin panel:

```
python manage.py createsuperuser
```

Follow the prompts to set up the admin account.

7. Run the development server

Start the Django development server:

```
python manage.py runserver
```

The app should now be running locally. Access it at `http://127.0.0.1:8000/` in your web browser. This will initially take you to the login page.
If you created a superuser, you can log in using your superuser account details. You can also log in to the admin panel at `http://127.0.0.1:8000/admin/`.

## Deployment Instructions (to PythonAnywhere)
1. Create an account on [PythonAnywhere](https://www.pythonanywhere.com/) and open a new __Bash Console__.

2. Clone the "deployed" branch with the following command:
```
git clone --single-branch --branch deployed https://github.com/goneal26/Newsies.git
```

This is the branch with the specific configurations for deployment to PythonAnywhere already in place.

Next, while in the parent directory of the file containing the cloned repository (path should be `/home/username/Newsies`), rename the "Newsies" directory to "newsies" with the following command:

```
mv Newsies newsies
```

__This is important for setting up the Web App configuration later.__

3. Create a virtual environment in the console with the following command:
```
mkvirtualenv --python=/usr/bin/python3.10 venv
```

If the virtual environment does not activate automatically (the current line in the bash console contains `(venv)$`), then run `source venv/bin/activate`. 

If you see an error saying `mkvirtualenv: command not found`, run the following two commands and try again:

```
echo '' >> ~/.bashrc && echo 'source virtualenvwrapper.sh' >> ~/.bashrc
source virtualenvwrapper.sh
```

4. Install dependencies

After activating your virtual environment, navigate into the main repository folder "newsies" and run `pip install -r requirements.txt`

5. Setting up web app and WSGI configuration

Leave the bash console and go to the __Web__ tab on PythonAnywhere and create a new web app, choosing the "Manual Configuration" option and the Python version you used for the virtual environment (in this case, 3.10).

Then, enter the name of the virtual environment (`venv`) in the __Virtualenv__ section and click OK.
The path to the virtualenv should be `/home/username/.virtualenvs/venv`, replacing "username" with your PythonAnywhere username.

In the __Code__ section of this page, enter the following path as the path to your *Source Code* and to your *Working Directory*: `/home/username/newsies`, replacing "username" with your PythonAnywhere username.

Click the link to the __WSGI configuration file__ underneath where you just entered the Code paths and replace the contents of the file with the following, and then save:

```
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/goneal26/mysite/mysite/settings.py'
# and your manage.py is is at '/home/goneal26/mysite/manage.py'
path = '/home/goneal26/newsies'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'newsies.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

6. Collect static files

Go back to your __Bash Console__ and navigate into the project folder (the one that contains `manage.py`) and run the following command:

```
python manage.py collectstatic
```

This will output the name of the static files directory. Copy this path and return to the __Web__ tab and enter it in the *Static files* section with the URL `/static/`. The path that you put in should look something like `/home/username/newsies/static/`.

7. Adding the RSS Fetching Task

Go to the __Tasks__ tab and add a new *Scheduled Task*. Set its frequency to *Daily* at whatever time you wish the RSS fetching to run every day, and set the *Command* to the path to the `jobs.py` script (should be something like `/home/username/newsies/features/jobs.py`). Add a description if you would like.

If the task is not automatically enabled, enable it after entering in this information with the "play" button on the right.

8. Setting up the database

From here, you can return to the bash console and run the `python manage.py migrate` to set up the database.

If you have any json dump files containing data from a previous database instance from a development build you may have been using for this project, you can upload them to the project directory under the __Files__ tab and load them to the database in the console with `python manage.py loaddata (filename).json`.

Then, if you want you can create a superuser, you can run the `python manage.py createsuperuser` command outlined earlier and follow the prompts.

Now just reload the website using the button in the __Web__ tab and navigate to the website URL (likely something like username.pythonanywhere.com) to see your deployed build of Newsies!

## Documentation
In the project's "features" and "users" apps you can find markdown files containing documentation for those apps/components (`features/FEATURE-DOCS.md` and `users/USER-DOCS.md`).

Documentation is also described using docstrings and code comments throughout the source code itself.

## Resources
### General development resources (Tre)
*(Including links to any GPT chats)*

 - https://chat.openai.com/share/01b8cacf-2d9c-471a-8ab3-7d22c8d34e8c
	- For minor refactors to the initial base.html
 - https://chat.openai.com/share/048ea012-e1c6-47e3-bf10-b292919caf96
 	- For initial feeds and CSS fixes for the base template
 - https://chat.openai.com/share/7dfe965c-2c2d-453c-a9ab-d4c0a8af7465
 	- For authentication and profile front-end components/debugging
 - https://chat.openai.com/share/1828faac-44f8-4d99-bb36-e8bd557ad3b6
 	- For learning CSS flex system
 - https://chat.openai.com/share/40f86916-052f-4c69-9850-ada049709ffe
 	- For model object annotation (for the following and upvoting features)
 - https://chat.openai.com/share/86b5648f-14e4-4e30-a84a-03be0ca13c73
 	- For tracking clicks (for counting articles read) through a modified form button (which I ended up using this style of component regularly)
 - https://chat.openai.com/share/37085bbe-1fc4-4de8-bd0a-72f99bb576b7
 	- For tag searching/searchbar view system
 - https://chat.openai.com/share/41932f06-4ae1-433a-a3e2-d7c6801eda5b
 	- Searchbar styling
 - https://chat.openai.com/share/44b93ade-cb65-4169-bc79-9a4951e362e0
 	- For clarifying details about dumping/loading data
 - https://stackoverflow.com/questions/70859953/how-to-update-my-django-database-with-rss-feed-every-x-minutes
 - https://medium.com/@jonathanmondaut/fetching-data-from-rss-feeds-in-python-a-comprehensive-guide-a3dc86a5b7bc
 	- Example implementations for RSS Fetching
 - https://apscheduler.readthedocs.io/en/3.x/userguide.html#code-examples
 	- Library documentation for scheduling RSS fetching
 	- As well as the Django documentation and the W3Schools django course if I needed to review something

### General development resources (Alexander)

Microsoft Copilot Prompts:
 - Create a views page in Python using Django for rendering article blurbs in a newsfeed application.
 - Create an HTML template for the discovery feed page of a newsfeed application.
 - Generate a CSS file for the above HTML file. (Discovery Feed)
 - Generate a JavaScript file for the above HTML file. (Discovery Feed)
 - Create a views page in Python using Django for fetching the pages a user follows in a newsfeed application.
 - Create an HTML template for the home feed page of a newsfeed application based on the following HTML template for the discovery feed page of the newsfeed application.
 - Generate a CSS file for the above HTML file. (Home Feed)
 - Generate a JavaScript file for the above HTML file. (Home Feed)
 - Create an HTML template for the login page of a newsfeed application.
 - Create a CSS file for the above HTML file for the login page.
 - Create a basic HTML and CSS template for a navbar.
 - How can I add a logo to this navbar?
 - Create a CSS file for the above HTML file for the navigation bar.
 - Create an HTML template for the news outlets page of a newsfeed application.
 - Generate a CSS file for the above HTML file. (Outlets Page)
 - Generate a JavaScript file for the above HTML file. (Outlets Page)
 - Create an HTML template for the register page of a newsfeed application.
 - Create an HTML template for the user profile page of a newsfeed application.
 - Create a CSS file for the above HTML file for the user profile page.
 - Modify the following HTML code for the discovery feed page of a newsfeed application to include a search bar that allows filtering
 - Design a Django application that allows a user to create, save and edit posts additionally view and like posts from other users.
 - Given the following HTML code, where should I add code to enable upvoting and downvoting?
 - Please add the following HTML code to the HTML code I gave you in the first prompt to enable upvoting/downvoting
 - Generate Django Python code for the comments section of a newsfeed application.
 - Generate Django Python code for a badge system of a newsfeed application where users earn a badge after reading a certain number of articles.
 - Generate Django Python code for a badge system of a newsfeed application that keeps track of the number of articles a user reads where users earn a badge after reading a certain number of articles.
 - Write Django Python code implementing the steps you mentioned above.

### Deployment resources (Tre)
 - https://help.pythonanywhere.com/pages/AlwaysOnTasks
 - https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata
 - https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
 - https://github.com/yourlabs/django-cities-light/issues/89
 - https://stackoverflow.com/questions/853796/problems-with-contenttypes-when-loading-a-fixture-in-django
