#!/usr/bin/env python3

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# user1 less right of connect but admin1 more right of connect
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# checks if name of user exist in dic of users
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        return username
    return None


@app.route("/login", methods=["POST"])
def user_login():
    # take name and password of user (request json)
    username = request.json["username"]
    password = request.json["password"]

    # search user in dic users
    user = users.get(username)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    # credentials are infos of idendity user

    access_token = create_access_token(
        identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token), 200


# for user1 and admin1
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


# for user1 and admin1
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


# for admin1
@app.route("/admin-only")
@jwt_required()
def admin_only():
    if get_jwt_identity()["role"] != "admin":
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted", 200


# errors of tokens
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
