# Makefile for the simple page server.
#

# Nothing to install for this project.
install:
	@(echo "Nothing to install")

start:
	@(bash start.sh)

stop:
	@(bash stop.sh; make clean)

run:
	@(make start)

clean:
	@(rm -f *.pyc; rm -rf __pycache__)

veryclean:
	@(rm -f ,pypid)
