from flask import Blueprint, render_template, request, redirect, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Note
from github_sync import push_note_to_github
from ai_tools import summarize_note, tag_note

routes = Blueprint('routes', __name__)

@routes.route("/")
@login_required
def index():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", notes=notes)

@routes.route("/add", methods=["POST"])
@login_required
def add_note():
    title = request.form["title"]
    content = request.form["content"]
    vault = request.form["vault"]
    summary = summarize_note(content)
    tags = tag_note(content)
    note = Note(user_id=current_user.id, title=title, content=content, tags=",".join(tags), vault=vault)
    db.session.add(note)
    db.session.commit()
    push_note_to_github(note)
    return redirect("/")

