from flask import *
# importing the author and the student blueprints
from routes.students_routes import *
from routes.authors_routes import *
from routes.book_routes import *

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# register of blue prints
app.register_blueprint(student_bp, url_prefix ="/student")
app.register_blueprint(author_bp, url_prefix="/author")
app.register_blueprint(book_bp, url_prefix="/book")

app.run(debug=True)