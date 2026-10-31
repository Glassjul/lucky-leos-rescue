 # Import the Flask class from the flask package
from flask import Flask, render_template

# Create the web app
app = Flask(__name__)

# When someone visits the home page ("/"), run this function
@app.route("/")
def welcome():
    # Build welcome.html and tell the header that "home" is the active page
    return render_template("welcome.html", active_page="home")

# Start the server only when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)