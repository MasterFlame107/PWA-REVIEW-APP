from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        elif len(note) > 300:
            flash('Note is too Long, 300 chracters Max', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user = current_user)
'''
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
'''
@views.route('/movies', methods=['GET','POST'])
@login_required
def Moviepage():
    return render_template("movie.html", user=current_user)
import requests
import tmdbsimple as tmdb
tmdb.API_KEY = '88efc50ea253d10e2b2edd2fb70f0ef6'

def movieset(code):
    movie = tmdb.Movies(code)
    response = (movie.info())
    name = (movie.title)
    budget = (f"${movie.budget}")
    synop = (response['overview'])
    poster = (f"https://image.tmdb.org/t/p/w500{response['poster_path']}")
    return [name, budget, synop, poster]

def movieroutes(id):
    @views.route(f'/movies/{id}', methods=['GET','POST'])
    @login_required
    def moviePage():
        return render_template('moviebase.html', movieInfo = movieset(id))
    
idList = [423,11220,406,103931,666277,577922,475557,155,13]
for element in idList:
    movieroutes(element)

