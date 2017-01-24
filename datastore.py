
import os
from book import Book

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0

def setup():
    ''' Read book info from file, if file exists. '''

    global counter

    try :
        with open(BOOKS_FILE_NAME) as f:
            data = f.read()
            make_book_list(data)
    except FileNotFoundError:
        # First time program has run. Assume no books.
        pass


    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                counter = int(f.read())
            except:
                counter = 0
    except:
        counter = len(book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''

    output_data = make_output_data()

    # Create data directory
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        pass # Ignore - if directory exists, don't need to do anything.

    with open(BOOKS_FILE_NAME, 'w') as f:
        f.write(output_data)

    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(counter))


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


def add_book(book):
    ''' Add to db, set id value, return Book'''

    global book_list

    book.id = generate_id()
    book_list.append(book)


def generate_id():
    global counter
    counter += 1
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

def make_book_list(string_from_file):
    ''' turn the string from the file into a list of Book objects'''

    global book_list

    books_str = string_from_file.split('\n')

    for book_str in books_str:
        data = book_str.split(separator)
        book = Book(data[0], data[1], data[2], data[3] == 'True', int(data[4]))
        book_list.append(book)


def make_output_data():
    ''' create a string containing all data on books, for writing to output file'''

    global book_list

    output_data = []

    for book in book_list:
        output = [ book.title, book.author, str(book.dateread), str(book.read), str(book.id) ]
        output_str = separator.join(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string
