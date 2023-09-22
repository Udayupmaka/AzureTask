from flask import Flask, render_template, request, redirect, url_for
from azure.identity import DefaultAzureCredential

app = Flask(__name__)

credential = DefaultAzureCredential()

# User registration and login functionality
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["Uday"]
        password = request.form["Uday1234"]

        # Register the user in the database

        return redirect(url_for("login"))
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["Uday"]
        password = request.form["Uday1234"]

        # Validate the user's credentials

        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html")

# Dashboard displaying user-specific information
@app.route("/dashboard")
def dashboard():
    # Get the user's information from the database

    return render_template("dashboard.html", user=user)

# RESTful API that allows users to perform CRUD operations on their data
@app.route("/api/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        # Get all users from the database

        return jsonify(users)
    else:
        # Create a new user in the database

        return jsonify(user)

@app.route("/api/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def user(user_id):
    if request.method == "GET":
        # Get the user with the specified ID from the database

        return jsonify(user)
    elif request.method == "PUT":
        # Update the user with the specified ID in the database

        return jsonify(user)
    else:
        # Delete the user with the specified ID from the database

        return jsonify(message="User deleted successfully")

if __name__ == "__main__":
    app.run(host="172.32.86.51", port=5000)
