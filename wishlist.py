#Main program

import ui, datastore, IO
from book import Book
book_list =[]
counter=0

def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        delete_unread()

    elif choice == '6':
        search()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')

def search():
    print('Enter the title of the book')
    sTitle = input()
    sbook = datastore.get_books(title = sTitle)
    print(str(sbook))

def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)

def delete_unread():
    # will get the user input and call the function to delete the book
    show_unread()
    book_deleted = ui.ask_for_book_id()
    datastore.delete_unread_book(book_deleted)

def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')


def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info(datastore.book_list)
    if (new_book==''):
        pass
    else:
        datastore.add_book(new_book)
        ui.message('Book added: ' + str(new_book))


def quit():
    '''Perform shutdown tasks'''
    IO.shutdown()
    ui.message('Bye!')


def main():

    IO.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
