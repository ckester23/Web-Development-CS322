# UOCIS322 - Project 0

Cheyanne Kester
ckester@uoregon.edu


Trivial project to exercise version control, turn-in, and other mechanisms
for CIS 322.

Please read this **thoroughly** before starting.

## Setting up Git

### Windows Users

If you're using Windows, please refer to this [link](https://www.howtogeek.com/336775/how-to-enable-and-use-windows-10s-built-in-ssh-commands/) for instructions on enabling SSH.

### Setting up keys

In order to access your GitHub repositories and commit changes,
you have to set up an SSH key first. This is more secure and convenient than using your GitHub username and password every time. Read more 
[here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

### Adding keys

Once you've created your keys and added them to your GitHub account, use the following command to add the key:
```
ssh-add path/to/.ssh/ssh_filename
```
You may also need to start an `ssh agent` every time you open a new terminal session:
```
eval $(ssh-agent)
```

### Installing git
You might already have git. Check `which git`.

If you don't, here's a tutorial on installing git: [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## General Instructions
These instructions also apply to every other project you will be doing this term. There's always a GitHub repository, like this one. You will be doing the following with EVERY project:

- Start by forking the repository on
[GitHub](https://github.com/UO-CIS322/project-0),
then cloning it locally.

- Read the instructions in `README` files (like this one). They clearly outline everything that needs to be done.

- Commit your changes and push.

- Test everything from scratch: clone elsewhere from scratch, run and make sure everything works as expected. It is recommended that you test it on the server we discussed at least once.

- Once you are done with each project, you will submit a `credentials.ini` file on Canvas. It contains your name and repository URL. An example of such a file is provided in this project: `credentials-skel.ini`.
	- BE CAREFUL with this file. Autograder reads this file, and can't correct your mistakes. If the URL is incorrect, or your name is not filled in, it will not grade your project. That is effectively the same as not turning in your project.
	- First time mistakes are can be overlooked, repeated ones will result in docking.

- You should not **ever** push `credentials.ini`. That file should only be submitted through Canvas.

## Project 0 Instructions

### Files needed to be edited
- `Makefile`

### Instructions

- Copy `credentials-skel.ini` it to `credentials.ini` and fill in appropriately.

- Modify the program so that it prints "Hello
  world", nothing more and nothing less.  Note that you should do this ONLY by adding a single line to `Makefile`, and modifying `credentials.ini`.

- Replace these instructions with a proper README including the
   author, contact address, and a brief description of what the
   software does.

- Test, commit, push, test again, and turn in.
   - Use `make install` to set up.
   - Use `make run` to run.
   - Use `git status` to monitor changes
   - Use `git add $FILE` to stage files (new and existing). 
   		- **DO NOT ADD/PUSH `credentials.ini`!**
   - Use `git commit -m $MESSAGE` to commit staged changes (those `add`ed) with a commit message.
   - Use `git push` to push local commits.
   - To test, clone elsewhere (the server), and test (do `make install` and `make run`), it should work as expected.
   - Turn the project in by submitting your **filled in** `credentials.ini` file to Canvas.


## Grading Rubric

* If everything works as expected, 100 will be assigned.
* If the correct message is not shown ("Hello World"), 20 points will be docked.
* If `make run` fails, 20 points will be docked.
* If `make install` fails, 20 points will be docked.
* If `credentials.ini` is commited, 10 points will be docked.
* If `README.md` is not updated with your name and info, 10 points will be docked.
* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.