#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def help_all(self):
        """Help information for the all command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        for k, v in storage.all().items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_quit(self, args):
        """Exit the HBNB console"""
        return True

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, args):
        """Handles EOF to exit program"""
        print()
        return True

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def do_create(self, args):
        """Create a new object of a given class with specified parameters."""
        if not args:
            print("** class name missing **")
            return


        args_list = args.split(' ')
        class_name = args_list[0]
        params = args_list[1:]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return


        obj_kwargs = {}
        for param in params:

            key_value = param.split('=')
            if len(key_value) != 2:
                print(f"Invalid parameter: {param}. Skipping...")
                continue

            key = key_value[0]
            value = key_value[1]


            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    print(f"Invalid float value: {value}. Skipping...")
                    continue
            else:

                try:
                    value = int(value)
                except ValueError:
                    print(f"Invalid integer value: {value}. Skipping...")
                    continue


        obj_kwargs[key] = value

        new_instance = self.classes[class_name](**obj_kwargs)
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """Help information for the create method"""
        print("Create a new object of a given class with specified parameters")
        print("Command syntax: create <Class name> <param 1> <param 2> <param 3>...")
        print("Param syntax: <key name>=<value>")
        print("Value syntax:")
        print("- String: \"<value>\" => starts with a double quote")
        print("  any double quote inside the value must be escaped with a backslash \\")
        print("  all underscores _ must be replace by spaces")
        print("- Float: <unit>.<decimal> => contains a dot .")
        print("- Integer: <number> => default case")
        print("If any parameter doesn't fit with these requirements or can't be recognized correctly by your program, it must be skipped")
        print("Don't forget to add tests for this new feature!")
    
    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        print_list = []

        if args:
            args = args.split(' ')[0] 
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
