import json

from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import current_user, login_required

from . import db
from .models import Note

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = (request.form.get("note") or "").strip()

        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            db.session.add(Note(data=note, user_id=current_user.id))
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)


@views.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    note_id = json.loads(request.data).get("noteId")
    note = db.session.get(Note, note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()

    return jsonify({})
