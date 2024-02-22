#!/usr/bin/env python3
"""
flask app module to interact with the authentication database.
"""


import email
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)

AUTH = Auth()


@app.route("/")
def index():
    """Index route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """Register a user in the database."""
    email = request.form["email"]
    password = request.form["password"]
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError as err:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """Login route"""
    email = request.form["email"]
    password = request.form["password"]
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if session_id:
            response = make_response(
                jsonify({"email": email, "message": "logged in"}), 200
            )
            response.set_cookie("session_id", session_id)
            return response
    abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """Logout route"""
    session_id = request.cookies.get("session_id")
    print(session_id)
    if session_id:
        AUTH.destroy_session(session_id)
        redirect("/")
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
