"""
Flask web site with vocabulary matching game
(identify vocabulary words that can be made
from a scrambled string)
"""

import flask
import logging
from flask import request

# Our modules
from src.letterbag import LetterBag
from src.vocab import Vocab
from src.jumble import jumbled
import src.config as config


###
# Globals
###
app = flask.Flask(__name__)

CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY  # Should allow using session variables

#
# One shared 'Vocab' object, read-only after initialization,
# shared by all threads and instances.  Otherwise we would have to
# store it in the browser and transmit it on each request/response cycle,
# or else read it from the file on each request/response cycle,
# neither of which would be suitable for responding keystroke by keystroke.

WORDS = Vocab(CONFIG.VOCAB)
SEED = CONFIG.SEED
try:
    SEED = int(SEED)
except ValueError:
    SEED = None


###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    """The main page of the application"""
    flask.g.vocab = WORDS.as_list()
    flask.session["target_count"] = min(
        len(flask.g.vocab), CONFIG.SUCCESS_AT_COUNT)
    flask.session["jumble"] = jumbled(
        flask.g.vocab, flask.session["target_count"], seed=None if not SEED or SEED < 0 else SEED)
    flask.session["matches"] = []
    app.logger.debug("Session variables have been set")
    assert flask.session["matches"] == []
    assert flask.session["target_count"] > 0
    app.logger.debug("At least one seems to be set correctly")
    return flask.render_template('vocab.html')

@app.route("/success")
def success():
    return flask.render_template('success.html')


#######################
# Form handler.
#   You'll need to change this to
#   a JSON request handler
#######################

# @app.route("/_check", methods=["POST"])
@app.route("/_check")
def check():
    """
    User has submitted the form with a word ('attempt')
    that should be formed from the jumble and on the
    vocabulary list.  We respond depending on whether
    the word is on the vocab list (therefore correctly spelled),
    made only from the jumble letters, and not a word they
    already found.

    flask send the new word to JS
    """

    app.logger.debug("Entering check")

    # The data we need, from cookie

    # text = flask.request.form["attempt"]
    text = request.args.get("text", type=str)

    # keep these since they don't do anything with form stuff
    jumble = flask.session["jumble"]
    matches = flask.session.get("matches", [])  # Default to empty list

    # a flag to help determine whether to append the word typed to html
    new_match = False

    # store messages and send using jsonify instead of flashing them
    msg = ""

    # Is it good?
    in_jumble = LetterBag(jumble).contains(text)
    matched = WORDS.has(text)

    # Respond appropriately
    if matched and in_jumble and not (text in matches):
        # Cool, they found a new word
        matches.append(text)
        flask.session["matches"] = matches
        msg=""
        new_match = True

    elif text in matches:
        # ERROR: does this when first correct word is typed after incorrect words..
        # first correct word off the bat after reload; and second when you've typed incorrect twice
        # flask.flash("You already found {}".format(text))
        msg="You already found " + text
        new_match = False

    elif not matched:
        # flask.flash("{} isn't in the list of words".format(text))
        msg=text + " isn't in the list of words"
        new_match = False

    elif not in_jumble:
        # flask.flash(
        #     '"{}" can\'t be made from the letters {}'.format(text, jumble))
        msg= text + " can't be made from the letters " + jumble
        new_match = False

    else:
        app.logger.debug("This case shouldn't happen!")
        new_match = False
        msg=""
        assert False  # Raises AssertionError
    
    # Choose page:  DO NOT REDIRECT IN FLASK
    # when game is over, JS is supposed to redirect to /success
    # that line of code is not given anywhere, you'll need to google it
    if len(matches) >= flask.session["target_count"]:
        if (new_match):
            return flask.jsonify(hello=matches, message="Success")
        else:
            return flask.jsonify(hello=[], message=msg)
    else:
        if (new_match) :
            return flask.jsonify(hello=matches, message="")
        else:
            return flask.jsonify(hello=[], message=msg)


###############
# AJAX request handlers
#   These return JSON, rather than rendering pages.
###############

@app.route("/_example")
def example():
    """
    Example ajax request handler
    """
    app.logger.debug("Got a JSON request")
    rslt = {"key": "value"}
    return flask.jsonify(result=rslt)


#################
# Functions used within the templates
#################

@app.template_filter('filt')
def format_filt(something):
    """
    Example of a filter that can be used within
    the Jinja2 code
    """
    return "Not what you asked for"

###################
#   Error handlers
###################


@app.errorhandler(404)
def error_404(e):
    app.logger.warning("++ 404 error: {}".format(e))
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


#############

if __name__ == "__main__":
    if CONFIG.DEBUG:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
        app.logger.info(
            "Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=CONFIG.DEBUG)
