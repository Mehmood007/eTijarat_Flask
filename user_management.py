import flask_pymongo,json
from bson import json_util
import uuid

#Connection with Database
try:
    mongo = flask_pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo.e_Tijarat
    
    
    mongo.server_info()
except:
    print("Error cannot connect to db")




def buyer_signUP(data):
    db.buyers.insert_one(data)
    return {"message":"User Signed Up successfully"}


def buyer_login(data):
    buyer = db.buyers.find({"email":data['email'],'password':data['password']})
    try:
        buyer = parse_json(buyer[0])
        session = dict(buyer['_id'])['$oid']+str(uuid.uuid4())
        db.sessions.insert_one({'session_id':session,'user_previliges':'buyer',"user_id": buyer["email"]})
        return buyer,session
    except IndexError:
        return False,False



def verify_buyer(session_id):
    user = db.sessions.find({"session_id": session_id})

    try:
        user = parse_json(user[0])
        if user['user_previliges'] == "buyer":
            buyer = parse_json(db.buyers.find({'email':user["user_id"]})[0])
            return buyer
        else:
            return False
    except:
        return False





def vendor_signUP(data):
    db.vendors.insert_one(data)
    return {"message":"User Signed Up successfully"}



def vendor_login(data):
    vendor = db.vendors.find({"email":data['email'],'password':data['password']})
    try:
        vendor = parse_json(vendor[0])
        session = dict(vendor['_id'])['$oid']+str(uuid.uuid4())
        db.sessions.insert_one({'session_id':session,'user_previliges':'vendor',"user_id": vendor["email"]})
        return vendor,session
    except IndexError:
        return False,False


def verify_vendor(session_id):
    user = db.sessions.find({"session_id": session_id})

    try:
        user = parse_json(user[0])
        if user['user_previliges'] == "vendor":
            vendor = parse_json(db.vendors.find({"email":user["user_id"]})[0])
            return vendor
        else:
            return False
    except:
        return False


def add_product(product):
    db.products.insert_one(product)


def parse_json(data):
    return json.loads(json_util.dumps(data))