"""
  A trivial web server in Python.

  Based largely on https://docs.python.org/3.4/howto/sockets.html
  This trivial implementation is not robust:  We have omitted decent
  error handling and many other things to keep the illustration as simple
  as possible.

  FIXME: DONE
  Currently this program always serves an ascii graphic of a cat.
  Change it to serve files if they end with .html or .css, and are
  located in ./pages  (where '.' is the directory from which this
  program is run).
"""
import os # me
import config    # Configure from .ini files and command line
import logging   # Better than print statements
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)
# Logging level may be overridden by configuration 

import socket    # Basic TCP/IP communication on the internet
import _thread   # Response computation runs concurrently with main program

def listen(portnum):
    """
    Create and listen to a server socket.
    Args:
       portnum: Integer in range 1024-65535; temporary use ports
           should be in range 49152-65535.
    Returns:
       A server socket, unless connection fails (e.g., because
       the port is already in use).
    """
    # Internet, streaming socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Bind to port and make accessible from anywhere that has our IP address
    serversocket.bind(('', portnum)) #'127.0.0.1' if you want localhost??
    serversocket.listen(1)    # A real server would have multiple listeners
    return serversocket


def serve(sock, func):
    """
    Respond to connections on sock.
    Args:
       sock:  A server socket, already listening on some port.
       func:  a function that takes a client socket and does something with it
    Returns: nothing
    Effects:
        For each connection, func is called on a client socket connected
        to the connected client, running concurrently in its own thread.
    """
    while True:
        log.info("Attempting to accept a connection on {}".format(sock))
        (clientsocket, address) = sock.accept()
        _thread.start_new_thread(func, (clientsocket,))


##
# Starter version only serves cat pictures. In fact, only a
# particular cat picture.  This one.
##
CAT = """Hello, you made it to the main page, here's a cat!
     ^ ^
   =(   )=
"""

# HTTP response codes, as the strings we will actually send.
# See:  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# or    http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
##
STATUS_OK = "HTTP/1.0 200 OK\n\n"
STATUS_FORBIDDEN = "HTTP/1.0 403 Forbidden\n\n"
STATUS_NOT_FOUND = "HTTP/1.0 404 Not Found\n\n"
STATUS_NOT_IMPLEMENTED = "HTTP/1.0 401 Not Implemented\n\n"

def respond(sock):
    """
    This server responds only to GET requests (not PUT, POST, or UPDATE).
    Any valid GET request is answered with either an ascii graphic of a cat,
    or the output from a file that matches the request (if such a file exists)
    """
    sent = 0
    request = sock.recv(1024)  # We accept only short requests
    request = str(request, encoding='utf-8', errors='strict')
    log.info("--- Received request ----")
    log.info("Request was {}\n***\n".format(request))

    parts = request.split()
    if len(parts) > 1 and parts[0] == "GET":
        print(request)
        if ".." in request or "~" in request:
            transmit(STATUS_FORBIDDEN, sock)
            transmit("Oops! The request contained forbidden characters `..` or `~`\n", sock)

        elif len(parts[1]) <= 1:
            # navigate to main page on empty requests: "/" or " "
            transmit(STATUS_OK, sock)
            transmit(CAT, sock) 

        else:
            cnt = 0

            # to access the files in our directory, use getcwd()
            for file in os.listdir(os.getcwd()):

                # I don't want non-useful files
                if file.endswith(".html") or file.endswith(".css"):

                    # check if the file we have matches the one requested
                    if ("/" + file) == parts[1]:
                        transmit(STATUS_OK, sock)

                        # now send the file's contents to display
                        opened = open(file, "r")
                        for line in opened.readlines():
                            transmit(line, sock)
                        opened.close()

                        cnt += 1 # this will help us in the next line

            # if we never found a matching file:       
            if cnt == 0:
                transmit(STATUS_NOT_FOUND, sock)
                transmit("Oops! I could not find that file\n", sock)
    
    else:
        log.info("Unhandled request: {}".format(request))
        transmit(STATUS_NOT_IMPLEMENTED, sock)
        transmit("\nI don't handle this request: {}\n".format(request), sock)
        # this section keeps acting weird; 
        # broken pipe in transmit() line 144: sent += sock.send(buff)

    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    return


def transmit(msg, sock):
    """It might take several sends to get the whole message out"""
    sent = 0
    while sent < len(msg):
        buff = bytes(msg[sent:], encoding="utf-8")
        sent += sock.send(buff)

###
#
# Run from command line
#
###


def get_options():
    """
    Options from command line or configuration file.
    Returns namespace object with option value for port
    """
    # Defaults from configuration files;
    #   on conflict, the last value read has precedence
    options = config.configuration()
    # We want: PORT, DOCROOT, possibly LOGGING

    if options.PORT <= 1000:
        log.warning(("Port {} selected. " +
                         " Ports 0..1000 are reserved \n" +
                         "by the operating system").format(options.port))

    return options


def main():
    options = get_options()
    port = options.PORT
    docroot = options.DOCROOT 

    # we need a way to access the files in docroot, so we'll change the 
    # current working directory!
    if docroot:
        os.chdir(docroot)

    if options.DEBUG:
        log.setLevel(logging.DEBUG)

    sock = listen(port)
    log.info("Listening on port {}".format(port))
    log.info("Socket is {}".format(sock))

    serve(sock, respond)

if __name__ == "__main__":
    main()
