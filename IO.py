import os
import json
import datastore
from book import Book
from jsonBook import jsonBook

DATA_DIR = 'data'
BOOKS_FILE_NAME = os.path.join(DATA_DIR, 'wishlist.txt')
COUNTER_FILE_NAME = os.path.join(DATA_DIR, 'counter.txt')

#separator = '^^^'  # a string probably not in any valid data relating to a book


def setup():
    ''' Read book info from file, if file exists. '''


    try :
        with open(BOOKS_FILE_NAME) as f:
            data = json.load(f)
        for line in data:
            newBook = jsonBook(line)
            datastore.book_list.append(newBook)
        for book in datastore.book_list:
            print(str(book))

            #datastore.make_book_list(data)
    except FileNotFoundError:
        # First time program has run. Assume no books.
        #pass
        print('file not found')
    #except:
        #pass


    try:
        with open(COUNTER_FILE_NAME) as f:
            try:
                datastore.counter = int(f.read())
            except:
                datastore.counter = 0
    except:
        datastore.counter = len(datastore.book_list)


def shutdown():
    '''Save all data to a file - one for books, one for the current counter value, for persistent storage'''
    #output_data = datastore.make_output_data()
    # ob=''
    jsonArray = []
    for book in datastore.book_list:
         jsonArray.append(book.toJSON())
    #     ob+='\n'
    with open(BOOKS_FILE_NAME, 'w') as f:
        # print(datastore.book_list)
        # f.write(ob)
         json.dump(jsonArray, f)


    with open(COUNTER_FILE_NAME, 'w') as f:
        f.write(str(datastore.counter))
    # Create data directory
    # try:
    #     os.mkdir(DATA_DIR)
    # except FileExistsError:
    #     pass # Ignore - if directory exists, don't need to do anything.
    #
    # with open(BOOKS_FILE_NAME, 'w') as f:
    #     f.write(output_data)
    #
    # with open(COUNTER_FILE_NAME, 'w') as f:
    #     f.write(str(counter))
