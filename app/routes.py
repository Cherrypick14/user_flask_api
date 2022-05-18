from flask import jsonify, request, abort
from app import app
from app.models import User, db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import unset_jwt_cookies

@app.route("/register", methods=["POST"])
def register():
    data= request.json

    name=data.get("name")
    username=data.get("username")
    company=data.get("company")
    jobtitle = data.get("jobtitle")
    email = data.get("email")
    password = data.get("password")

    error={}

    if not name:
       error["name"] ="Name is required"
    if not username:
       error["name"] ="username is required"
    if not company:
       error["name"] ="company is required"
    if not jobtitle:
       error["name"] ="jobtitle is required"
    if not email:
       error["name"] ="email is required"
    if not password:
       error["name"] ="password is required"
  
    if len(error.keys()) != 0:
       abort(400, {error:"error"})
    user= User(name=name,username=username,company=company,jobtitle=jobtitle,email=email,password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    return {"message":"user created"}, 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    
    email = data.get("email")
    password = data.get("password")
    
    user= User.query.filter_by(email=email).first()

    if user:
        response =check_password_hash(user.password, password)
        if response:
            access_token= create_access_token(identity={"name":user.name, "company":user.company, "jobtitle":user.jobtitle})
            return jsonify (access_token=access_token),200
        else:
            return {"message":"invalid"},400

@app.route("/home", methods=["GET"])
@jwt_required()
def home():
    identity = get_jwt_identity()
    return identity

@app.route("/update/<id>", methods=["PUT"])
@jwt_required()
def update(id):
    data= request.json
    user = User.query.filter_by(id=id).first()
    if user:
        user.username = data.get("username")
        user.company = data.get("company")
        user.jobtitle= data.get("jobtitle")

        db.session.commit()
        return {"message": "user successfully updated"}, 200
    return {"message": "user not found"}

@app.route("/delete/<id>", methods=["POST"])
@jwt_required()
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify("user successfully deleted")

@app.route("/logout", methods=["GET","POST"])
@jwt_required()
def log_out():
    response = jsonify('user logged out')
    unset_jwt_cookies(response)
    return response, 200


