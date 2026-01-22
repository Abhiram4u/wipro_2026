from flask import Flask, jsonify, request

app = Flask(__name__)

details = [{"id":1,"name":"abhi","email":"abhi@gmail.com"},
           {"id":2,"name":"arun","email":"arun@gmail.com"},
           {"id":3,"name":"varma","email":"varma@gmail.com"}]

@app.route("/", methods=["Get"])
def home():
    return "Welcome"
@app.route("/details",methods=["Get"])
def get_users():
    return jsonify(details)

if __name__ == "__main__":
    app.run(debug=True)
