from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, JWTManager
from flask import Blueprint, request, jsonify
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

revoked_tokens = set()

jwt = JWTManager()


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    revoked_tokens.add(jti)
    return jsonify({"message": "Token has been revoked"}), 200


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in revoked_tokens
