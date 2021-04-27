from flask import Flask, render_template
from flask_cors import CORS

from routes import routes

# Initialise the site
app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the routes
app.register_blueprint(routes)


@app.errorhandler(404)
def not_found(e):
    return render_template("not-found.html"), 404


# Start the site
if __name__ == "__main__":
    app.run(debug=True)
