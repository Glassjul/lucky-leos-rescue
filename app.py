 # Import the Flask class from the flask package
from flask import Flask, render_template, request
from dogs import DOGS, BREEDS
from filters import filter_by_breed

# Create the web app
app = Flask(__name__)

# When someone visits the home page ("/"), run this function
@app.route("/")
def welcome():
    # Build welcome.html and tell the header that "home" is the active page
    return render_template("welcome.html", active_page="home")

# When someone visits /dogs, show the adoptable dogs page
@app.route("/dogs")
def dogs():
    # Read the chosen breed from the URL, for example /dogs?breed=Beagle
    # If there is no breed in the URL, use an empty string (All breeds)
    selected_breed = request.args.get("breed", "")

    # Keep only the dogs that match the chosen breed
    shown_dogs = filter_by_breed(DOGS, selected_breed)

    return render_template(
        "dogs.html",
        active_page="dogs",
        dogs=shown_dogs,
        breeds=BREEDS,
        selected_breed=selected_breed,
    )

# Start the server only when this file is run directly
if __name__ == "__main__":
    app.run(debug=True, port=5001)