#  AirBnB clone - The console
![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/25884337/140618660-12cbf53d-6ab2-4f48-9f3a-32cda5a23817.png)
## Description of the project
The goal of the project is to deploy a replica of Airbnb website using my
server It will not implement all the features, just some of them to cover all
the fundamental concepts.
In this case a command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

#### Functionalities:
* Create a new object as User or Place
* Retrieve an object from a file.
* Update attributes of an object
* Destroy an object

## Installation
* Clone this repository
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## Files and directories
[console.py](console.py) - Contains the entry point of the command interpreter. 
* `EOF` - Exits console 
* `quit` - Exits console
* `<emptyline>` - Does nothing
* `create` - Creates a new instance of object and saves it into .JSON file
* `destroy` - Deletes an object from specific .JSON file
* `show` - Prints the string representation of an specific object.
* `all` - Prints all string representation of all available objects .
* `update` - Updates an objects based on the class name and id.

#### `models/`
[base_model.py](/models/base_model.py) - The BaseModel class
* `def __init__(self, *args, **kwargs)` - Initialization of class
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

#### `/models/engine` serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes and deserializes objects
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key
* `def save(self)` - serializes __objects to the JSON file
* ` def reload(self)` -  deserializes the JSON file to __objects

## Authors
Sandra Lorena - [Twitter](https://twitter.com/alexa_orrico)  
Manuel Gomez - [Twitter](https://twitter.com/ManoloGomez08)
