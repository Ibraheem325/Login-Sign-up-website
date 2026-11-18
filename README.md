# Login & Sign-Up Website

A small Flask web app with user accounts and a personal notes page. I built it to practise
backend basics: routing, authentication, and storing data in a SQL database.

**Live demo:** https://login-signup-website-lqfx.onrender.com
(free hosting, so the first load after a period of inactivity can take up to about a minute)

## What it does

- Sign up, log in and log out. Passwords are stored hashed, never as plain text.
- Pages that need an account redirect to the login page.
- Logged-in users can add and delete their own notes.

## What it uses

- **Flask** for routes, blueprints and Jinja2 templates
- **Flask-Login** for user sessions
- **SQL via SQLAlchemy**: two tables, `User` and `Note`, linked by a one-to-many relationship
  through a foreign key. The app uses SQLite locally and Postgres in the deployed version.
- **Bootstrap** and a little JavaScript for the front end

Originally written with Python 3.11; the deployed version runs on Python 3.12.

## Project structure

```
main.py              starts the app
website/
  __init__.py        app setup: config, database, login manager
  models.py          User and Note tables
  auth.py            login, logout and sign-up routes
  views.py           notes page and delete-note route
  templates/         HTML pages
  static/index.js    sends the delete-note request
```

## Run locally

```bash
git clone https://github.com/Ibraheem325/Login-Sign-up-website.git
cd Login-Sign-up-website
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py            # open http://127.0.0.1:5000
```

A local SQLite database is created automatically on first run.
