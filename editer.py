import ui, datastore
#show list of books for user to edit
def editItem():
    editBook=''
    blist=datastore.get_books()
    ui.show_list(blist)
    print('Choose a book to edit')
    #get user choice
    boid= ui.ask_for_book_id()
    for book in blist:
        #validate user input
        if (book.id == boid):
            editBook=book

        else:
            print('ID not found')
    #identify which attribute to edit
    edch = getEditChoice()
    #edit object and replace it in the datastore book_list
    processChoice(edch, editBook)

def getEditChoice():
    print('What would you like to edit?')
    print('1. Title')
    print('2. Author')
    print('3. Date Read')
    print('4. Review')

    while True:
        try:
            edAtt= int(input())
            if edAtt >= 0:
                return edAtt
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')

def processChoice(value, book):
    if value == 1:
        print ('Enter new title data')
        datastore.book_list.remove(book)
        book.title = input()
        datastore.book_list.append(book)

    elif value == 2:
        print ('Enter new Author data')
        datastore.book_list.remove(book)
        book.author = input()
        datastore.book_list.append(book)

    elif value == 3:
        print ('Enter new date data')
        datastore.book_list.remove(book)
        book.dateread = input()
        datastore.book_list.append(book)

    elif value == 4:
        datastore.book_list.remove(book)
        book.review = input()
        datastore.book_list.append(book)
