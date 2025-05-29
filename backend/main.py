# create
# - first_name
# - last_name
# - email

# localhost:5000 -> domain /create_contace -> end point
# Request [Front End]: type: GET >access, POST > create, PATCH >update, DELETE >delete
# return json: {}
# Response [Back End]: status: 200> success, 404> not found, 400> bad request
# return json:{}

from flask import request, jsonify, render_template
from config import app, db
from models import User

@app.route("/users", methods=["GET"])  # access
def get_infos():
    infos = User.query.all()    # get all contacts
    json_infos =  list(map(lambda x: x.to_json(), infos))   # Function that create new list from contacts
    return jsonify({"infos": json_infos})

@app.route("/signup", methods=["POST"])
def create_infos():
    first_name = request.json.get("firstName")  # get the value of using the dict
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:    # if does not exist
        return (
            jsonify({"message":"You must include a first name, last name, and email"}), 
            400,
        )

    new_account = User(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_account)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created!"}), 201

@app.route("/update_user-info/<int:user_id>", methods=["PATCH"])    # path parameter
def update_user_info(user_id):
    infos = User.query.get(user_id)

    if not infos:
        return jsonify({"message":"User not found"}), 404
    
    data = request.json
    infos.first_name = data.get("firstName", infos.first_name)
    infos.last_name = data.get("lastName", infos.last_name)
    infos.email = data.get("email", infos.email)

    db.session.commit()

    return jsonify({"message": "User Updated"}), 200

@app.route("/delete-user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    infos = User.query.get(user_id)

    if not infos:
        return jsonify({"message":"User not found"}), 404
    
    db.session.delete(infos)
    db.session.commit()

    return jsonify({"message":"User Deleted"}), 200

@app.route("/home/<firstName>-<lastName>")
def home(firstName, lastName):
    return render_template("index.html")


if __name__ == "__main__":  # to run the file directly, and get run when this file is imported
    with app.app_context(): # instanciate the database
        db.create_all()

    app.run(debug=True)