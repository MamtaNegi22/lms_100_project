from flask import *

book_bp=Blueprint("book", __name__)

@book_bp.route("/create-book")
def create_book():
    return "create the new book here"


# def ''