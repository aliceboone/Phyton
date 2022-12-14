from abc import ABC
from datetime import datetime
from enum import Enum
import self as self


# Enums and Constants: Here are the required enums, data types, and constants:

class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7


class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4


class ReservationStatus(Enum):
    WAITING, COMPLETED, PENDING, CANCELED, NONE = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person(ABC):
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


class Constants:
    self.MAX_BOOK_ISSUED_TO_A_USER  = 5
    self.MAX_LENDING_DAYS = 10


# Account, Member, and Librarian: These classes represent various people that interact with our system:

class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person

    def reset_password(self):
        None


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)

    def add_cook_item(selfself, book_item):
        None

    def block_menber(self, member):
        None

    def un_block_member(self, member):
        None


class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)
        self.__date_of_menbership = datetime.date.today()
        self.__total_books_checkedout = 0

    def get_total_books_checkout(self):
        return self.__total_books_checkedout

    def reserve_book_item(self, book_item):
        None

    def increment_total_books_checkedout(self):
        None

    def rebew_book_item(self, book_item):
        None

    def checkout_book_item(self, book_item):
        if self.get_total_books_checkout() >= Constants.MAX_BOOK_ISSUED_TO_A_USER:
            print("The user has already checked out maximum number of books")
            return False
        book_reservation = BookReservation.fetch_reservation_details(book_item.getbarcode())
        if book_reservation != None and book_reservation.get_member_id() != self.get_id():
            # book item has a pending reservation from another user
            print("self book is reserved by another user")
            return False
        elif book_reservation != None:
            # book item has a pending reservation from the give member, update it
            book_reservation.update_status(ReservationStatus.COMPLETED)

        if not book_item.checkout(self.get_id()):
            return False

        self.increment_total_books_checkedout()
        return True

    def check_for_fine(self, book_item_barcode):
        book_lending = BookReservation.fetch_lending_details(book_item_barcode)
        due_date = book_lending.get_due_date()
        today = datetime.date.today()
        # check if the book has been returned within the due date
        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_Number_id(), diff_days)

    def return_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(
            book_item.get_barcode())
        if book_reservation != None:
            # book item has a pending reservation
            book_item.update_book_item_status(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
        book_item.update_book_item_status(BookStatus.AVAILABLE)

    def renew_book_item(self, book_item):
        self.check_for_fine(book_item.getbarcode())
        book_reservation = BookReservation.fetch_reservation_details(book_item.getbarcode)
        # check if self book item has a pending reservation from another member
        if book_reservation != None and book_reservation.get_member_id() != self.get_member_id():
            print("self book is reserved by another member")
            self.decrement_total_books_checkedout()
            book_item.update_book_item_state(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            return False
        elif book_reservation != None:
            book_reservation.update_status(ReservationStatus.COMPLETED)
        BookLending.lend_book(book_item.getbarcode(), self.get_member_id())
        book_item.update_due_date(datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
        return True


# BookReservation, BookLending, and Fine: These classes represent a book reservation, lending, and fine collection, respectively.
class BookReservation:
    def __init__(self, creation_date, status, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__status = status
        self.__book_item_barcode = book_item_barcode
        self.__init__member_id = member_id

    def fetch_reservation_details(self, barcode):
        None


class BookLending:
    def __init__(self, creation_date, due_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__return_date = None
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def lend_book(self, barcode, member_id):
        None

    def fetch_lending_details(self, barcode):
        pass


class Fine:
    def __init__(self, creation_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__book_item_id = book_item_barcode
        self.__member_id = member_id

    def collect_fine(self, member_id, days):
        None


# BookItem: Encapsulating a book item, this class will be responsible for processing the reservation, return, and renewal of a book item.

class Book(ABC):
    def __init__(self, ISBN, title, subject, publisher, language, number_of_pagers):
        self.__ISBN = ISBN
        self.__title = title
        self.subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__number_of_pages = number_of_pagers
        self.authors = []


class BookItem(Book):
    def __init__(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status, date_of_purchase,
                 publication_date, placed_at):
        self.__barcode = barcode
        self.__is_reference = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__price = price
        self.__book_format = book_format
        self.__status = status
        self.date_of_purchase = date_of_purchase
        self.__puclication_date = publication_date
        self.__placed_at = placed_at

    def checkout(self, member_id):
        if self.get_is_reference_only():
            print("self book is reference only and can't be issued")
            return False
        if not BookLending.lend_book(self.__get_barcode(0), member_id):
            return False
        self.update_book_item_status(BookStatus.LOANED)
        return True


class Rack:
    def __init__(self, number, location_identifier):
        self.__number = number
        self.__location_identifier = location_identifier


# Search interface and Catalog: The Catalog class will implement the Search interface to facilitate searching of books.

class Search(ABC):
    def search_by_title(self, title):
        None

    def search_by_author(self, author):
        None

    def search_by_subject(self, subject):
        None

    def search_by_pub_date(self, puclish_date):
        None


class Catalog(Search):
    def __init__(self):
        self.__book_title = {}
        self.__authors = {}
        self.__subjects = {}
        self.__book_publication_date = {}

    def search_by_title(self, query):
        # return all books containing the string query in their title.
        return self.__book_title.get(query)

    def search_by_author(self, query):
        # return all books containing the string query in their author's name.
        return self.__book_author.get(query)
