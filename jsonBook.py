import json
from book import Book
#book subclass to allow for alternate constructor method for book object
class jsonBook(Book):
    def __init__(self, j):
        self.__dict__=json.loads(j)
