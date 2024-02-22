#!/usr/bin/env python3
"""
flask app module to interact with the authentication database.
"""


import email
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
