from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user = current_user)
'''
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
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
    genre = []
    for g in response['genres']:
       genre.append(g['name'])
    return [name, budget, synop, poster, genre]


@views.route('/movies/423', methods=['GET','POST'])
@login_required
def moviePage_pianist():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        elif len(note) > 300:
            flash('Note is too Long, 300 chracters Max', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id, movie_page="pianist", user_name=current_user.first_name)  #providing the schema for the note 
            
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')
    movienotes = Note.query.filter_by(movie_page="pianist").all()
    print(movienotes)

    return render_template('moviebase.html', movieInfo = movieset(423), user=current_user, movie_notes = movienotes)

@views.route('/movies/11220', methods=['GET','POST'])
@login_required
def moviePage_fallenangels():
    return render_template('moviebase.html', movieInfo = movieset(11220), user=current_user)

@views.route('/movies/406', methods=['GET','POST'])
@login_required
def moviePage_lahaine():
    return render_template('moviebase.html', movieInfo = movieset(406), user=current_user)

@views.route('/movies/103931', methods=['GET','POST'])
@login_required
def moviePage_duvidha():
    return render_template('moviebase.html', movieInfo = movieset(103931), user=current_user)

@views.route('/movies/666277', methods=['GET','POST'])
@login_required
def moviePage_pastlives():
    return render_template('moviebase.html', movieInfo = movieset(666277), user=current_user)

@views.route('/movies/577922', methods=['GET','POST'])
@login_required
def moviePage_tenet():
    return render_template('moviebase.html', movieInfo = movieset(577922), user=current_user)

@views.route('/movies/475557', methods=['GET','POST'])
@login_required
def moviePage_joker():
    return render_template('moviebase.html', movieInfo = movieset(475557), user=current_user)

@views.route('/movies/155', methods=['GET','POST'])
@login_required
def moviePage_darkKnight():
    return render_template('moviebase.html', movieInfo = movieset(155), user=current_user)

@views.route('/movies/13', methods=['GET','POST'])
@login_required
def moviePage_forrestGump():
    return render_template('moviebase.html', movieInfo = movieset(13), user=current_user)
    

