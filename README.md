This is the first step towards building our first full web application:
the AirBnB clone.
what we are using now is the seed with all other following projects:
HTML/CSS templating, database storage, API, front-end integration…

we put in place a parent class (called BaseModel) to take care of the
initialization, serialization and deserialization of future instances

Then, we create a simple flow of serialization/deserialization: Instance
<-> Dictionary <-> JSON string <-> file

Then, we create all classes used for AirBnB (User, State, City, Place…) that
inherit from BaseModel

create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

This project consists of 11 mandatory tasks

how to start the project:
usage:
./console.py

to see all available commands
./console.py
>> help

Quit command to exit the program

(hbnb) 
(hbnb) quit

example of usage
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
