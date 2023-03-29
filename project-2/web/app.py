"""
Cheyanne Kester's Flask API.
"""

from flask import Flask, abort, send_from_directory
import os
import configparser

app = Flask(__name__)

def parse_config(config_paths): 
    # from project-0 hello.py
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

#app route function
@app.route("/<path:request>")
def hello(request):
    # make sure the request is legal first
    if "~" in request or ".." in request:
        abort(403)

    # now search for the requested file in /pages
    for file in os.listdir("./pages"):

        # I don't want non-useful files
        if file.endswith(".html") or file.endswith(".css"):

            # check if the file we have matches the one requested
            if (file) == request:
                # now send the file
                return send_from_directory('pages/', file);
    
    # if we haven't found and returned a file yet 
    abort(404)

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def notfound(e):
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    config = parse_config(["credentials.ini", "default.ini"])
    PORT = config["SERVER"]['PORT']
    DEBUG = config["SERVER"]['DEBUG']

    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
