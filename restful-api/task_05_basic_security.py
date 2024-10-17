#!/usr/bin/env python3

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

app = Flask(__name__)
app.config["SECRET_KEY"] = "Test"
app.config["JWT_SECRET_KEY"] = "Test"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users_db = {
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


@auth.verify_password
def authenticate_user(username, password):
    user_recup = users_db.get(username)
    if user_recup and check_password_hash(user_recup['password'], password):
        return user_recup
    return None


@app.route('/basic-auth')
@auth.login_required
def basic_protected_route():
    return jsonify(message="Basic Auth: Access Granted")


@app.route('/token-login', methods=['POST'])
def generate_jwt_token():
    login_data = request.get_json()
    user_recup = users_db.get(login_data.get('username'))

    if user_recup and check_password_hash(
        user_recup['password'], login_data.get('password')
    ):
        jwt_token = create_access_token(
            identity={'username': user_recup['username'],
                      'role': user_recup['role']}
        )
        return jsonify(access_token=jwt_token)
    return jsonify(error="Invalid login details"), 401


@app.route('/jwt-protected-route')
@jwt_required()
def jwt_protected_route():
    return jsonify(message="JWT Auth: Access Granted")


@app.route('/admin-only-route')
@jwt_required()
def admin_only_route():
    currt_id = get_jwt_identity()
    if currt_id['role'] != 'admin':
        return jsonify(error="Admin access required"), 403
    return jsonify(message="Admin Access: Granted")


@jwt.unauthorized_loader
def handle_missing_token(_):
    return jsonify(error="Authorization token is missing or invalid"), 401


@jwt.invalid_token_loader
def handle_invalid_token(_):
    return jsonify(error="Invalid token provided"), 401


@jwt.expired_token_loader
def handle_expired_token(_):
    return jsonify(error="Your token has expired"), 401


@jwt.revoked_token_loader
def handle_revoked_token(_):
    return jsonify(error="The token has been revoked"), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_required(_):
    return jsonify(error="A fresh token is required for this action"), 401


if __name__ == "__main__":
    app.run()
