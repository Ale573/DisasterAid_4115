from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

from config import app
from handler.user import UserHandler




@app.route('/')
def hello_world():
    return 'Welcome to Disaster Aid Distribution App!'

@app.route("/DAD/register", methods=['POST'])
def registerUser():
    return UserHandler().insertUser(request.json)

@app.route("/DAD/user", methods=['GET'])
def getAllUsers():
    return UserHandler().getAllUsers()

@app.route('/DAD/user/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return UserHandler().getUserById(uid)
    elif request.method == 'PUT':
        return UserHandler().updateUser(uid, request.json)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run(debug = True)
