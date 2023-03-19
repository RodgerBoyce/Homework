from models.book import *


library = [Book("The Old Man and the Sea", "Ernest Hemingway", "Fiction"), 
           Book("The Hobbit", "J.R.R Tolkien", "Fiction"), 
           Book("A Brief History of Time", "Stephen Hawking", "Popular Science"), 
           Book("Treasure Island", "Robert Louis Stevenson", "Fiction")]


def add_book(book):
    library.append(book)


def remove_book(library, title):
    for book in library:
        if book.title == title:
            library.remove(book)
            return True
    return False