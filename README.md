0x00 AirBnB clone | The Console
Description of the project:
This is the starting point of the AirBnB clone project, where we focused on setting up the project's backend and connecting it to a console application using Python's cmd module.

The data, represented as Python objects, is stored in a JSON file and can be accessed using Python's json module.

Description of the command interpreter:
The command interpreter works similar to the Bash shell but is tailored for specific commands needed for the AirBnB website. It acts as the user interface, allowing interaction with the backend developed in Python using object-oriented programming.

Key commands include:

-show -create -update -destroy -count

In this command line interpreter, along with the backend and file storage system, you can perform actions like creating new objects (such as a User or a Place), retrieving objects from files or databases, conducting operations on objects (count, compute stats, etc.), updating object attributes, and destroying objects.

How to start it
Follow these steps to get the project on your local machine (Linux). It's for development and testing purposes.

Installing
git clone https://github.com/Phve/AirBnB_clone.git 
Change to 'Airbnb' directory and run the command:

./console.py
How to use it
It can work in two different modes:

Interactive.
The console will display a prompt (hbnb) hinting the user can execute and write a command. After running the command, what will appear again will be the prompt and a wait for new command. As long as the user does not exit the program, it can go continually

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
Non-interactive.
At the initiation of the shell, smoothly execute it by piping a command input. No prompt shall surface, and user input is unnecessary. The specified command will promptly unfold as the shell enters this mode of silent execution.

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
The command Input's input
In Non-Interactive Mode for commands in silent mode, echo them through. The console will get it done. Elsewhere, Interactive Mode chats with the console by typing commands. Hit enter, and the console acts. To leave, use CTRL + D, CTRL + C, or say quit or EOF.

Author
"Ashton Muiru" "James Maina"
