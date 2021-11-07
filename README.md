#  AirBnB clone - The console
![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/25884337/140618660-12cbf53d-6ab2-4f48-9f3a-32cda5a23817.png)
## Description of the project
The goal of the project is to deploy a replica of the Airbnb website using my
server It will not implement all the features, just some of them to cover all
the fundamental concepts.
In this segment we create a shell to manage the AirBnB website objects.


## files and directorioes

- models:the directory that will contain all the classes used for the whole
project
- console.py:this is the file that will contain the main console.
- tests:this file contains unit tests
- base_model.py:is responsible for the initialization, serialization and
deserialization of future instances... atributes: id, created_at. updated_at
metodos save(), to_json
- engine:
- file_storage.py:this file contains the file storage class.

## description of the command interpreter

Basic Usage of The Console

| commands | usage | functionality |
------ |------ |------ |
| create | create <clase> |creates new object a new user,plece |
| help | help |display all commands available |
| quit | quit |exists|
| all | user.all() |display all objectsin class|
| destroy | user.destroy(123)|destroys specified object|
|show | user.sow(123) |shows a specific instance|
|update| user. update(123,{name :name@mail.com})|updates attributes of an object|