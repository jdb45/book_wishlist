
import os

import json


#DATA_DIR = 'data'
#BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
#COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')
from book import Book

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0


def get_books(**kwargs):
    ''' Return books from data store. With no arguments, returns everything. '''

    global book_list

    if len(kwargs) == 0:
        return book_list

      # giving the user the option to sort the books in a specific way
    if 'read' in kwargs:
        print('''
      1. Sort by Title
      2. Sort by Author
      3. Sort by book ID
          ''')
        user_sort = input('Enter your selection: ')
        # taking the user choice and displaying the list
        if user_sort == '1':
            book_list = sorted(book_list, key=lambda book: book.title)
            read_books = [book for book in book_list if book.read == kwargs['read']]
            return read_books

        elif user_sort == '2':
            book_list = sorted(book_list, key=lambda book: book.author)
            read_books = [book for book in book_list if book.read == kwargs['read']]
            return read_books

        else:
            book_list = sorted(book_list, key=lambda book: book.id)
            read_books = [book for book in book_list if book.read == kwargs['read']]
            return read_books
    #allows for search function by title
    elif 'title' in kwargs:
        for book in book_list:
            if book.title == kwargs['title']:
                return book


def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id()
    book_list.append(book)


def generate_id():
    global counter
    global book_list
    book_list = sorted(book_list, key=lambda book: book.id)

    counter = len(book_list)-1
    try:
        bid= book_list[counter]
        counter = bid.id+1
    except IndexError:
        #handle empty list error
        counter = 1
    return counter


def set_read(book_id, read):
    '''Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise.'''

    global book_list

    for book in book_list:
    # added a input to get the user input of the date they read the book
         if book.id == book_id:
            book.read = True
            get_review = input('Would you like to enter a review of the book? yes or no?')
            if get_review.lower().startswith("y"):
                user_review = input('Enter review here:')
                book.review = user_review
            else:
                book.review = 'None Given'
            user_date = input("Please enter the date you read the book:")
            book.dateread = user_date
            return True

    return False # return False if book id is not found

def delete_unread_book(book_id):
    # function to remove an unread book from the list
    global book_list

    for book in book_list:
        if book.id == book_id:
            book_list.remove(book)
            print("Successfully removed", book.title, "from the unread book list")




def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    for book in book_list:
        output = [ book.title, book.author, str(book.dateread), book.review, str(book.read), str(book.id) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string
