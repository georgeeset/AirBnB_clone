#!/usr/bin/python3
'''
the entry point of the command interpreter
'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    command interpreter for AirBnB project with commands to be used
    '''
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

    prompt = "(hbnb)"

    def do_EOF(self, line):
        '''end of file marker used to exit the program
        '''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def emptyline(self):
        '''executes nothing
        '''
        pass

    def do_create(self, line):
        '''
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        Example: $ create BaseModel
        '''
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        newinst = BaseModel()
        newinst.save()
        print(newinst.id)

    def do_show(self, line):
        '''
        Prints the string representation of an instance
        based on the class name and id
        Example: $ show BaseModel 1234-1234-1234
        '''
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        objects_dict = storage.all()
        if f"{line_list[0]}.{line_list[1]}" not in objects_dict:
            print("** no instance found **")
            return
        print(objects_dict[f"{line_list[0]}.{line_list[1]}"])

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id
        save the change into the JSON file
        Example: $ destroy BaseModel 1234-1234-1234
        '''
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        objects_dict = storage.all()
        if f"{line_list[0]}.{line_list[1]}" not in objects_dict:
            print("** no instance found **")
            return
        del storage.all()[f"{line_list[0]}.{line_list[1]}"]
        storage.save()

    def do_all(self, line):
        '''
        Prints a list of all string representation of all instances
        based or not on the class name
        Example: $ all BaseModel or $ all
        '''
        line_list = line.split()
        if len(line_list) == 0:  # if no arg is passed to all command
            print([str(v).replace('\\', '') for v in storage.all().values()])
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(line_list) > 0:
            print([str(v).replace('\\', '') for v in storage.all().values()
                  if type(v).__name__ == line_list[0]])

    def do_update(self, line):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute (then saves change into the JSON file)
        Example: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        '''
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        objects_dict = storage.all()
        if f"{line_list[0]}.{line_list[1]}" not in objects_dict:
            print("** no instance found **")
            return
        if len(line_list) < 3:
            print("** attribute name missing **")
            return
        if len(line_list) < 4:
            print("** value missing **")
            return
        try:
            # strip off str ndcheck if int
            if isinstance(eval(line_list[3]), int):
                line_list[3] = int(line_list[3])
            elif isinstance(eval(line_list[3]), float):  # or if float
                line_list[3] = float(line_list[3])
            elif isinstance(eval(line_list[3]), str):  # or if float
                line_list[3] = line_list[3].replace('"', '')
        except NameError:
            line_list[3] = line_list[3]
        setattr(storage.all()[f"{line_list[0]}.{line_list[1]}"],
                line_list[2], line_list[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
