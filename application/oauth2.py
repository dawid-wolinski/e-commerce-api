from flask import jsonify, request
from functools import wraps
import jwt
from models import User
from datetime import datetime, timedelta
from database import app


# Credit to: https://www.geeksforgeeks.org/using-jwt-for-user-authentication-in-flask/


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=int(app.config['ACCESS_TOKEN_EXPIRE_MINUTES']))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, app.config['SECRET_KEY'], algorithm=app.config['ALGORITHM'])

    return encoded_jwt


# Validates access token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if token == None:
            return jsonify(error='Access token is missing')

        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[app.config['ALGORITHM']])
            current_user = User.query.filter_by(id=payload.get("user_id")).first()

        except:
            return jsonify(error='Invalid access token'), 401

        return f(current_user, *args, **kwargs)
    
    return decorated