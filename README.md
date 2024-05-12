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

7. Setting up the database

From here, you can run the `python manage.py migrate` to set up the database.

If you have any json dump files containing data from a previous database instance from a development build you may have been using for this project, you can upload them to the project directory under the __Files__ tab and load them to the database in the console with `python manage.py loaddata (filename).json`.

Then, if you want you can create a superuser, you can run the `python manage.py createsuperuser` command outlined earlier and follow the prompts.

Now just reload the website using the button in the __Web__ tab and navigate to the website URL (likely something like username.pythonanywhere.com) to see your deployed build of Newsies!