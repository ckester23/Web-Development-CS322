# UOCIS322 - Project 1 #

This project will get you started with creating a simple webpage server.

Cheyanne Kester
This project contains a program that runs a simple webpage server, that either 
outputs an ASCII representation of a cat, or, if the user makes a request, outputs 
whatever content is described in the `.html` or `.css` file matching that request (if such a file exists).

## Getting started

Directory structure:

* the "pages" (HTML files and their assets) will be located in DOCROOT. For this project that location is the `pages/` directory. Make sure you specify this in your `credentials.ini`!

* Everything that's located in `pageserver/`. That consists of a Python application (`pageserver.py`) that starts listening at a specified port and handles requests. This is the key file you'll be editing for this project.

* There's a configuration parser, much like the one seen in [project-0](https://github.com/UO-CIS322/project-0), but a more detailed version. It not only looks for your `credentials.ini` file, both in `pageserver/` and the parent directory and falls back to `default.ini` if missing, it also allows you to override those settings through CLI. These will be discussed in the lab.

* `Makefile` here refers to the two scripts provided: `start.sh` and `stop.sh`. The former starts the server, by calling `pageserver.py`. It will also store its PID (process id), in order to kill it later through `stop.sh`. However, if you notice that it failed to do so, you can kill it manually by looking up the PID.

## Tasks

The goal of this project is to implement a "file checking" logic for the existing server. Currently, if you set it up and start the server, it will just serve a page with a cat figure. What is expected is for the server to handle the requests as follows:

* If a file exists in `pages/` (i.e. `trivia.html`, any name, any extention or format) exists, transmit `200 OK` header followed by that file. If the file doesn't exist, transmit `404 Not Found` error code in the header along with a message in the body explaining further. If a request includes illegal characters (`..` or `~`), the response should be a `403 Forbidden` error, again with a message in the body explaining it.

* Update `README` with your name, info, and a brief description of the project.

* You will submit your credentials.ini in Canvas. It should include your name and repo URL.


## Grading Rubric

* If everything works as expected, 100 will be assigned.
* If existing pages and files are NOT handled correctly, 30 points will be docked.
* For each of the errors not handled correctly (403, and 404), 15 points will be docked.
* If `README.md` is not updated with your name and info, 10 points will be docked.
* If `credentials.ini` is commited, 10 points will be docked.
* If the repo clones, but `make install` or `make run` throws an error, 10 will be assigned.
* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.

## Authors

Michal Young, Ram Durairajan.