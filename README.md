# Login & Sign-Up Website

A small full-stack web app built with **Flask**. Users can create an account, log in, and keep a private list of notes. Notes are stored per user and can be added or deleted from the browser.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Ibraheem325/Login-Sign-up-website)

## Features

- **Sign-up with validation.** Checks for a unique email, a minimum name and password length, and a matching password confirmation.
- **Secure passwords.** Passwords are hashed with `scrypt` (Werkzeug). Plain-text passwords are never stored.
- **Session handling.** Login, logout and "remember me" sessions use Flask-Login. Protected routes redirect to the login page.
- **Per-user notes.** Users can create notes, and only the owner can delete them (AJAX `fetch` → JSON endpoint).
- **Feedback messages.** Success and error alerts use Flask's message flashing.
- **Responsive UI.** The layout uses Bootstrap 4 and Jinja2 template inheritance.
- **Database.** By default the app uses SQLite. Set `DATABASE_URL` to switch to Postgres in production.

## Tech stack

| Layer    | Tools                                     |
|----------|-------------------------------------------|
| Backend  | Python 3.12, Flask, Flask-Login           |
| Database | SQLAlchemy (SQLite locally, Postgres optional) |
| Frontend | Jinja2 templates, Bootstrap 4, vanilla JS |
| Serving  | Gunicorn                                  |

## Project structure

```
main.py                  entry point (creates the Flask app)
website/
  __init__.py            app factory: config, database, blueprints, login manager
  models.py              User and Note models
  auth.py                /login, /logout, /sign-up
  views.py               / (notes page) and /delete-note
  templates/             base, login, sign-up and home pages
  static/index.js        delete-note request
render.yaml              Render deployment blueprint
Procfile                 process definition for Heroku-style hosts
```

## Run locally

```bash
git clone https://github.com/Ibraheem325/Login-Sign-up-website.git
cd Login-Sign-up-website
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py            # http://127.0.0.1:5000
```

The SQLite database is created automatically in `instance/database.db` on first run.

## Configuration

| Variable       | Purpose                                                        | Default            |
|----------------|----------------------------------------------------------------|--------------------|
| `SECRET_KEY`   | Signs session cookies. Set a fixed value in production.        | random per start   |
| `DATABASE_URL` | SQLAlchemy URL, e.g. a Postgres connection string.             | local SQLite file  |

## Deployment

The app is deployed on [Render](https://render.com)'s free tier using `render.yaml`. Click the button above, or create a *Blueprint* from this repository in the Render dashboard.

- **The app sleeps when idle.** On Render's free plan it goes to sleep after a period without traffic, so the first visit afterwards can take a few seconds to load.
- **SQLite data doesn't last.** Render's free disk is reset when the app restarts, which wipes the SQLite database. To keep accounts permanently, create a free Postgres database (for example on [Neon](https://neon.tech)) and set its connection string as `DATABASE_URL`.
