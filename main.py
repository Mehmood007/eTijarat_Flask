from email import message
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import user_management

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return jsonify({"message":"Heloooo World!!!"})




#Buyer routes
@app.route("/signup", methods = ['POST'])
def signUp():
    buyer_details = request.get_json()
    if user_management.buyer_signUP(buyer_details):
        return jsonify({"message":"User Signed UP successfully"})
    return jsonify({"message":"Error in signing up franchise"})


@app.route("/login", methods = ['POST'])
def login():
    buyer_details = request.get_json()
    login,session_id = user_management.buyer_login(buyer_details)
    if login:
        return jsonify(login),{'session_id':session_id}
    return jsonify({"message":"Error in signing in franchise"})


@app.route("/verify_buyer")
def verify_buyer():
    session_id = request.headers['session_id']
    buyer = user_management.verify_buyer(session_id)
    if buyer:
        return jsonify(buyer)
    return jsonify({"message":"Invalid session_id"})


#Vendors routes
@app.route("/vendor_signup", methods = ['POST'])
def vendor_signUp():
    buyer_details = request.get_json()
    if user_management.vendor_signUP(buyer_details):
        return jsonify({"message":"User Signed UP successfully"})
    return jsonify({"message":"Error in signing up franchise"})


@app.route("/vendor_login", methods = ['POST'])
def vendor_login():
    vendor_details = request.get_json()
    login,session_id = user_management.vendor_login(vendor_details)
    if login:
        return jsonify(login),{'session_id':session_id}
    return jsonify({"message":"Error in signing in franchise"})


@app.route("/verify_vendor")
def verify_vendor():
    session_id = request.headers['session_id']
    vendor = user_management.verify_vendor(session_id)
    if vendor:
        return jsonify(vendor)
    return jsonify({"message":"Invalid session_id"})


@app.route("/add_product", methods = ['POST'])
def add_product():
    session_id = request.headers['session_id']
    vendor = user_management.verify_vendor(session_id)
    if vendor:
        product = request.get_json()
        user_management.add_product(product)
        return jsonify({"message":"Product added successfully"})
    return jsonify({"message":"Invalid session_id"})


if __name__ =="__main__":
    app.run(debug=True)