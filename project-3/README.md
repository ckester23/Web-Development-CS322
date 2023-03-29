# UOCIS322 - Project 3 #

Cheyanne Kester
This is a project to get familiar with JQuery and asynchronous requests using AJAX.

To do this, I programmed a vocab game in which the user is given a list of words, and a list of jumbled letters. The user must then type in words that they think can be made using only letters in the jumbled list, and which are also in the list of words given. The program tells the user whether or not their attempted word was successful (a part of the solution), and upon 3 successful attempts, a success page is loaded.


You'll learn about JQuery and asynchronous requests in this project.

## Overview

The program is a simple anagram game designed for English-learning students in elementary and middle school. It presents a list of words to students and an anagram. The anagram is a jumble of some of the words, which are randomly chosen. Students attempt to type words that can be created from the jumble. When a matching word is typed, it is added to a list of solved words.

The vocabulary word list is fixed for one invocation of the server, so multiple students connected to the same server will see the same vocabulary list but may have different anagrams.

## Getting started

`flask_vocab.py` runs the anagram game, with the template `vocab.html`. This example uses a conventional interaction through a form, interacting only when the user submits the form. The vocabulary and anagram are currently loaded using basic JINJA. What you're supposed to do is to change the form interaction into an AJAX interaction (using JQuery).

## Tasks

* Familiarize yourself with `flask_vocab.py` and `flask_minijax.py` by running them separately. You need to understand them to do this project.

* Your task is to replace the form interaction (in `flask_vocab.py`) with AJAX interaction on each keystroke using `flask_minijax.py`. 

  **NOTE:** You MUST remove the submit button, check for validity per keystroke, and redirect to the success page as soon as the required number of words are found.

* As always, revise the README file, and add your info to `Dockerfile`. These have points!

* As always, submit your `credentials.ini` through Canvas. It should contain your name and git repo URL.

## FAQ
### What is `src`?
This is a sub-package which contains modules related to the game. You should not make any changes there, but feel free to review them to get a better understanding.

### What is `data`?
This directory contains a few word lists in the form of text files. You should not make any changes to the ones that already exist. However, you can add your own (but don't have to). You can change the word list file in your `credentials.ini`.

### What is minijax?

`flask_minijax.py`, along with its template `templates/minijax.html`, is a tiny example of using JQuery with flask for an AJAX application. They should not be included in the version of the project you turn in. You can use this example to figure out how to implement an AJAX version of the game. Delete the two (along with `static/img`) when you're done with the project.

### How do I run the tests?
The `tests` directory contains a test suite for the `src` package. There's a `run_tests.sh`, which you can run in your container while it's running. However, it is not required, since you will not be changing anything in `src`.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
	* AJAX in the frontend (`vocab.html`)
	* Logic in the backend (`flask_vocab.py`)
	* Frontend to backend interaction (with correct requests and responses) between `vocab.html` and `flask_vocab.py`.
	* Basically the webpage should handle validation WITHOUT any refreshes.
* If the game isn't fully functional as described, **40 point** will be docked.

* If messages are not displayed correctly in the webpage, 30 points will be docked. Expected behavior is notifying whether (a) the word typed is not in the vocabulary, or (b) the word cannot be made from the anagram; and in the case of a match, the word should be written somewhere along with the rest of the matched words.

* If none of the functionalities work, 30 will be assigned assuming
    * `credentials.ini` is submitted with the correct URL of your repo,
    * `Dockerfile` builds without any errors, and an instance runs without crashing.
    * `Dockerfile` and `README` are updated with your name and email.

* If the `Dockerfile` doesn't run, build or is missing, 5 will be assigned.

* If `credentials.ini` is not submitted or the repo is not found, 0 will be assigned.
	 

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.