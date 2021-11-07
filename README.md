#  AirBnB clone - The console
![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/25884337/140618660-12cbf53d-6ab2-4f48-9f3a-32cda5a23817.png)
## Description of the project
The goal of the project is to deploy a replica of Airbnb website using my
server It will not implement all the features, just some of them to cover all
the fundamental concepts.
In this segment we create a shell to manage the AirBnB website objects.


## Files and directories

- models: the directory that will contain all the classes used for the whole
project
- console.py: this is the file that will contain the main console.
- tests: this folder contains unit tests
- base_model.py: is responsible for the initialization, serialization and
deserialization of future instances... atributes: id, created_at. updated_at
metodos save(), to_json
- engine: this folder contains the files that allow store tha data.
- file_storage.py: this file contains the file storage class.

## Description of the command interpreter

Basic Usage - Interpreter

| commands | usage | functionality |
------ |------ |------ |
| create | create "class_name" |create new instances ex: create User |
| help | help |display all commands available |
| quit | quit |exit of interpreter|
| all | all "class_name" |display all objects related to specific class ex: all User|
| destroy | destroy "id" |destroy specified object by id|
| show | show "id" |shows a specific instance|
| update | update "class_name" "id" "new_key" "new_value"|updates attributes of an object|