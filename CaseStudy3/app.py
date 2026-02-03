from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    },
{
        "id": 102,
        "movie_name": "kalki",
        "language": "Telugu",
        "duration": "3h",
        "price": 250
    },
{
        "id": 103,
        "movie_name": "Akasham nee Hadhura",
        "language": "Tamil",
        "duration": "2h 50m",
        "price": 150
    }

]

bookings = []

@app.route("/", methods=["Get"])
def home():
    return "Welcome"
# GET all movies
@app.route("/movies", methods=["Get"])
def get_movies():
    return jsonify(movies)

# GET movie by ID
@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie)
    return jsonify({"error": "Movie not found"}),404

# POST add new movie
@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    movies.append(data)
    return jsonify(data)

# PUT update movie
@app.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify(movie)
    return jsonify({"error": "Movie not found"}), 404

# DELETE movie
@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404

# POST book tickets
@app.route("/bookings", methods=["POST"])
def book_ticket():
    data = request.get_json()
    movie_id = data.get("movie_id")
    seats = data.get("seats")

    for movie in movies:
        if movie["id"] == movie_id:
            booking = {
                "movie_id": movie_id,
                "seats": seats,
                "total_price": movie["price"] * seats
            }
            bookings.append(booking)
            return jsonify(booking)

    return jsonify({"error": "Booking failed. Movie not found"}), 400
# get bookings
@app.route("/bookings", methods=["Get"])
def get_bookings():
    return jsonify(bookings)



if __name__ == "__main__":
    app.run(debug=True)
