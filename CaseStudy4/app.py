from flask import Flask, jsonify, request

app = Flask(__name__)

patients = []

# GET all patients
@app.route("/patients", methods=["GET"])
def get_all_patients():
    return jsonify(patients), 200


# POST register a patient
@app.route("/patients", methods=["POST"])
def register_patient():
    data = request.get_json()

    if not data.get("id") or not data.get("name"):
        return jsonify({"error": "Invalid patient data"}), 400

    patients.append(data)
    return jsonify(data), 201


# GET patient by ID
@app.route("/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    for patient in patients:
        if patient["id"] == pid:
            return jsonify(patient), 200
    return jsonify({"error": "Patient not found"}), 404


# PUT update patient info
@app.route("/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    data = request.get_json()
    for patient in patients:
        if patient["id"] == pid:
            patient.update(data)
            return jsonify(patient), 200
    return jsonify({"error": "Patient not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
