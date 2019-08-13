# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
Create and save new instance of BaseModel
`create HBNHCommand`
Ex:
`create BaseModel`

#### Show
Prints the string representation of an instance
`show HBNHCommand do_show`
Ex:
`show User my_id`

#### Destroy
Deletes an instance based on the class name and id
`destroy HBNHCommand do_destroy`
Ex:
`destroy Place my_place_id`

#### All
Prints all the string representations of all instances
`all` or `all HBHNHCommand`
Ex:
`all` or `all State`

#### Quit
Terminates current user session
`quit` or `EOF`

#### Help
Provides documentation and information to user
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `HBNHCommand.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

####Authors/Contributors
Adam Sedlki 720@Holbertonschool.com
Mia L. Morton 740@Holbertonschool.com
vagrant@vagrant-ubuntu-trusty-64:/vagrant/Dropbox/HOLBERTON/Adam-Of-Earth-AirBnB_clone-v2$ ^C
vagrant@vagrant-ubuntu-trusty-64:/vagrant/Dropbox/HOLBERTON/Adam-Of-Earth-AirBnB_clone-v2$ ls
AirBnB_clone-v2
vagrant@vagrant-ubuntu-trusty-64:/vagrant/Dropbox/HOLBERTON/Adam-Of-Earth-AirBnB_clone-v2$ cd AirBnB_clone-v2/
vagrant@vagrant-ubuntu-trusty-64:/vagrant/Dropbox/HOLBERTON/Adam-Of-Earth-AirBnB_clone-v2/AirBnB_clone-v2$ ls
AUTHORS  console.py  file.json  models  README.md  tests  web_static
vagrant@vagrant-ubuntu-trusty-64:/vagrant/Dropbox/HOLBERTON/Adam-Of-Earth-AirBnB_clone-v2/AirBnB_clone-v2$ emacs README.md 
















































File Edit Options Buffers Tools Help                                                               
# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can b\
e used to store objects in and retrieve objects from a JSON.

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`
