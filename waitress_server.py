from waitress import serve

from __init__ import app

serve(app, host="localhost", port="5000")
