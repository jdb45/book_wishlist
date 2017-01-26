import json
from book import Book
class jsonBook(Book):
    def __init__(self, j):
        self.__dict__=json.loads(j)
