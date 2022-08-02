from datetime import datetime
import time
# declare a new class for book instance
from Person import Author

class Book:
    def __init__(self,id, title, categoryId, da, copy, price):
        self._id = str(id)
        self._title = title
        self._category_id = categoryId
        self._publication_date = datetime(da, 1, 1)
        self._copies_owned = copy
        self._available_copies = copy
        self._price = price
        print("An book with ID: %s has added" % self._id)

    # to make change in book
    def set_title(self,title):
        self._title = title

    def setPublicationDate(self,date):
        self._publication_date = date

    def setCopiesOwned(self, copy):
        self._status = copy

    def setBookPrice(self, price):
        self._price = price

    def updateAvalibleCopies(self):
        self._available_copies = self._available_copies - 1

        # to query about book

    def get_bookid(self):
        return self._id

    def get_title(self):
        return self._title

    def getCategoryId(self):
        return self._category_id

    def getPublicationDate(self):
        return self._publication_date

    def getCopiesOwned(self):
        return self._copies_owned

    def getBookPrice(self):
        return self._price

    def getAvailableCopies(self):
        return self._available_copies

    #To Display Book Details
    def getBookDetials(self):
        return {
            "id": self._id,
            "title": self._title,
            "Category ID": self._category_id,
            "Publication Date": self._publication_date,
            "Copies Owned": self._copies_owned,
            "Price" : self._price
        }

class BookAuthor:
    def __init__(self,book_id , author_id ):
        self._book_id = book_id
        self._author_id = author_id

    def getBookAuthorDetails(self):
        return {
            "Book ID" : self._book_id,
            "Author ID" : self._author_id
        }


class Category:
    def __init__(self, id, name):
        self._id = id
        self._category_name = name

    def setCategoryName(self, name):
        self._category_name

    def getCategoryName(self):
        return self._category_name

    def getCategoryId(self):
        return self._id

    def getCategoryDetails(self):
        return{
            "Category ID" : self._id,
            "Category Name" : self._category_name
        }

