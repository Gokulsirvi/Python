"""
This is the SMALLEST POSSIBLE Django project in ONE file.
Run using: python main.py runserver
"""

import os
import django
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.urls import path
from django.shortcuts import redirect
from django import forms
from django.db import models

# ------------------------------------------------------
# DJANGO SETTINGS — Everything in one place
# ------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY="xyz123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "__main__",    # our file is our app
    ],
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],
    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # templates directly in code
        "APP_DIRS": True,
    }],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
)

django.setup()  # initialize Django


# ------------------------------------------------------
# MODEL (Database Table)
# ------------------------------------------------------
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# ------------------------------------------------------
# FORM (User Form)
# ------------------------------------------------------
class UserForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")


# ------------------------------------------------------
# VIEWS
# ------------------------------------------------------
def home(request):
    return HttpResponse("""
        <h1>Django One Page Project</h1>
        <ul>
            <li><a href='/form'>Form Page</a></li>
            <li><a href='/users'>Users List</a></li>
            <li><a href='/api/data'>API JSON</a></li>
        </ul>
    """)


def user_form(request):
    """Handles form submit + save to DB"""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
            )
            return redirect("/users")
    else:
        form = UserForm()

    return HttpResponse(f"""
        <h2>User Form</h2>
        <form method="POST">
            {form.as_p()}
            <button type="submit">Submit</button>
        </form>
    """)


def user_list(request):
    """Show all users"""
    users = User.objects.all()

    html = "<h2>Registered Users</h2>"
    for u in users:
        html += f"<p>{u.id} — {u.name} — {u.email}</p>"
    return HttpResponse(html)


def api_data(request):
    """Sample API"""
    return JsonResponse({"status": "success", "data": "Hello from Django!"})


# ------------------------------------------------------
# URLS
# ------------------------------------------------------
urlpatterns = [
    path("", home),
    path("form", user_form),
    path("users", user_list),
    path("api/data", api_data),
]


# ------------------------------------------------------
# RUN SERVER (like manage.py)
# ------------------------------------------------------
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line()
