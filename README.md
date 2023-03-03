# UOCIS322 - Project 6 #
Brevet time calculator with MongoDB, and a RESTful API!

Read about MongoEngine and Flask-RESTful before you start: [http://docs.mongoengine.org/](http://docs.mongoengine.org/), [https://flask-restful.readthedocs.io/en/latest/](https://flask-restful.readthedocs.io/en/latest/).

## Before you begin
You *HAVE TO* copy `.env-example` into `.env` and specify your container port numbers there!
Note that the default values (5000 and 5000) will work!

*DO NOT PLACE LOCAL PORTS IN YOUR COMPOSE FILE!*

## Overview

You will reuse your code from Project 5, which already has two services:

* Brevets
	* The entire web service
* MongoDB

For this project, you will re-organize `Brevets` into two separate services:

* Web (Front-end)
	* Time calculator (basically everything you had in project 4)
* API (Back-end)
	* A RESTful service to expose/store structured data in MongoDB.

## Tasks

* Implement a RESTful API in `api/`:
	* Write a data schema using MongoEngine for Checkpoints and Brevets:
		* `Checkpoint`:
			* `distance`: float, required, (checkpoint distance in kilometers), 
			* `location`: string, optional, (checkpoint location name), 
			* `open_time`: datetime, required, (checkpoint opening time), 
			* `close_time`: datetime, required, (checkpoint closing time).
		* `Brevet`:
			* `length`: float, required, (brevet distance in kilometers),
			* `start_time`: datetime, required, (brevet start time),
			* `checkpoints`: list of `Checkpoint`s, required, (checkpoints).
	* Using the schema, build a RESTful API with the resource `/brevets/`:
		* GET `http://API:PORT/api/brevets` should display all brevets stored in the database.
		* GET `http://API:PORT/api/brevet/ID` should display brevet with id `ID`.
		* POST `http://API:PORT/api/brevets` should insert brevet object in request into the database.
		* DELETE `http://API:PORT/api/brevet/ID` should delete brevet with id `ID`.
		* PUT `http://API:PORT/api/brevet/ID` should update brevet with id `ID` with object in request.

* Copy over `brevets/` from your completed project 5.
	* Replace every database related code in `brevets/` with calls to the new API.
		* Remember: AutoGrader will ensure there is NO CONNECTION between `brevets` and `db` services. `brevets` should only operate through `api` and still function the way it did in project 5.
		* Hint: Submit should send a POST request to the API to insert, Display should send a GET request, and display the last entry.
	* Remove `config.py` and adjust `flask_brevets.py` to use the `PORT` and `DEBUG` values specified in env variables (see `docker-compose.yml`).

* Update README.md with API documentation added.

As always you'll turn in your `credentials.ini` through Canvas.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
    * API routes as outlined above function exactly the way expected,
    * Web application works as expected in project 5,
    * README is updated with the necessary details.

* If the front-end service does not work, 20 points will be docked.

* For each of the 5 requests that do not work, 15 points will be docked.

* If none of the above work, 5 points will be assigned assuming project builds and runs, and `README` is updated. Otherwise, 0 will be assigned.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
