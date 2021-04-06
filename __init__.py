from flask import Flask

from routes import routes

# Initialise the site
app = Flask(__name__)

# Load the routes
app.register_blueprint(routes)

# Start the site
if __name__ == "__main__":
    app.run(debug=True)
