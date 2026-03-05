from flask import *
student_bp =Blueprint("student", __name__)  # this needs to be called in the main python file

@student_bp.route("/student-register")
def student_register():
    return "Register here for students."


@student_bp.route("/student-login")
def student_login():
    return "Login here for students."