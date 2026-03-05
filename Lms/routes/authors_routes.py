from flask import *

author_bp=Blueprint("author", __name__) # this is the most important line ,-- this need to be served to the app.py
# the 
@author_bp.route("/author-register")

def author_register():
    return "Register here for authors."

@author_bp.route("/author-login")
def author_login():
    return "Login here for author."