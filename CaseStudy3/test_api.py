import requests

BASE_URL = "http://127.0.0.1:5000/"

def test_get_movies():
    response = requests.get(f"{BASE_URL}movies")
    assert response.status_code == 200
    # Validate JSON response
    assert isinstance(response.json(), list)

def test_add_movie():
    payload = {
        "id": 105,
        "movie_name": "Avatar",
        "language": "English",
        "duration": "2h 42m",
        "price": 300
    }
    response = requests.post(f"{BASE_URL}movies", json=payload)
    assert response.status_code == 200
    # Validate JSON response
    response_json = response.json()
    assert response_json["movie_name"] == "Avatar"
    assert response_json["price"] == 300

def test_booking():
    payload = {
        "movie_id": 101,
        "seats": 2
    }
    response = requests.post(f"{BASE_URL}bookings", json=payload)
    assert response.status_code == 200

    # Validate JSON response
    response_json = response.json()
    assert response_json["movie_id"] == 101
    assert response_json["seats"] == 2
    assert response_json["total_price"] == 500
