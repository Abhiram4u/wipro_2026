import requests
import pytest


def test_fetch_all_patients(base_url):
    response = requests.get(base_url)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_register_patient(base_url):
    payload = {
        "id": 1,
        "name": "ABHI",
        "age": 30,
        "gender": "Male",
        "contact": "987878789",
        "disease": "Fever",
        "doctor": "Dr. Smith"
    }

    response = requests.post(base_url, json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "ABHI"


def test_get_patient_details(base_url):
    response = requests.get(f"{base_url}/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_patient(base_url):
    payload = {
        "disease": "Viral Fever"
    }

    response = requests.put(f"{base_url}/1", json=payload)

    assert response.status_code == 200
    assert response.json()["disease"] == "Viral Fever"


def test_invalid_patient(base_url):
    response = requests.get(f"{base_url}/999")

    assert response.status_code == 404
