# Create a simple RESTful API using Flask that manages a list of users.

# 1. Create a Flask application
# GET /users → Return all users
# GET /users/<id> → Return user details by ID
# POST /users → Create a new user
# 3. Follow REST principles:
# Return responses in JSON format
# 4. Store data in an in-memory list or dictionary


from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id":1,"name":"abhiram","email":"abhi@gmail.com"},
    {"id":2,"name":"arun","email":"arun@gmail.com"}
]

@app.route("/users", methods=["GET"])
def user_details():
    return jsonify(users),200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
        return jsonify({"error": "user not found"}),404

@app.route("/users",methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"message": "missing required fields"}), 400

    new_user = {"id":len(users)+1,
                "name":data.get("name"),
                "email":data.get("email")
                }
    users.append(new_user)
    return jsonify(new_user),201

if __name__ == "__main__":
    app.run(debug=True)



