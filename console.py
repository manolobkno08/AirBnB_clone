#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

"""
Admin Console

"""


class HBNBCommand(cmd.Cmd):
    """Interpreter"""
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel
    }

    def do_create(self, args):
        """Create instances"""
        args = args.split(' ')
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    # def do_show(self, args):
    #     """Print instances"""
    #     args = args.split(' ')
    #     if len(args) == 0:
    #         print("** class name missing **")
    #     if args in HBNBCommand.classes:
    #         if len(args) > 1:
    #             key = args[0] + "." + args[1]
    #             if key in models.storage.all():
    #                 print(models.storage.all()[key])
    #             else:
    #                 print("** no instance found **")
    #         else:
    #             print("** instance id missing **")
    #     else:
    #         print("** class doesn't exist **")

    def do_EOF(self, args):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_empty_(self):
        """Empty Line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
