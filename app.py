 # Import the Flask class from the flask package
from flask import Flask

# Create the web app
app = Flask(__name__)

# When someone visits the home page ("/"), run this function
@app.route("/")
def welcome():
    return "Lucky Leo's Rescue is running"

# Start the server only when this file is run directly
if __name__ == "__main__":
    app.run(debug=True)