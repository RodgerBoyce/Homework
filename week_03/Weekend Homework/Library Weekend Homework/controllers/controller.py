from flask import render_template, request, redirect
from app import app
from models.book import *
from models.library import library, add_book, remove_book

@app.route('/library')
def index():
    return render_template('index.html', title='Home', library=library)

@app.route('/library', methods=['POST'])
def add_new_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre'] 
    new_book = Book(title, author, genre)
    add_book(new_book)
    return redirect('/library')    

@app.route('/library/<book>')
def book(book):
    return render_template('book.html', title="Your Selected Book", book=library[int(book)])

@app.route('/remove-book', methods=['POST'])
def remove_book():
    title = request.form['title']
    for book in library:
        if book.title == title:
            library.remove(book) 
    return redirect('/library')

@app.route('/check-out-book', methods=['POST'])
def check_out_book():
    title = request.form['title']
    checked_out = 'checked_out' in request.form
    for book in library:
        if book.title == title:
            book.checked_out = checked_out
            break
    return redirect('/library')
