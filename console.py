#!/usr/bin/python3
"""
    A class that inherits from the cmd.Cmd class. This class is used to define
    the commands available in the HBNB console.

    Attributes:
        prompt (str): The prompt string used in the console.

    Methods:
        do_quit -- Command to exit the program
        do_EOF -- Exiting using EOF
        emptyline -- Do nothing on empty line
 """
import cmd
import sys
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    A class that inherits from the cmd.Cmd class. This class is used to define
    the commands available in the HBNB console.

    Attributes:
        prompt (str): The prompt string used in the console.

    Methods:
        do_quit -- Command to exit the program
        do_EOF -- Exiting using EOF
        emptyline -- Do nothing on empty line
    """

    prompt = '(hbnb) '

    project_classes = [
            "User",
            "State",
            "City",
            "Place",
            "BaseModel",
            "Amenity",
            "Review"]

    def default(self, line):
        """ default function for cmd interpter """
        if "\"" in line:
            line = line.replace("\"", "")

        command = line.split(".")
        dictionary = storage.all()
        count = 0

        if command[0] in HBNBCommand.project_classes and command[1] == "all()":
            self.do_all(command[0])

        elif command[0] in HBNBCommand.project_classes and command[
                1] == "count()":

            for key, value in dictionary.items():
                if value.__class__.__name__ == command[0]:
                    count = count + 1
            print(count)
        # Update console.py to retrieve an instance based on its ID:
        # <class name>.show(<id>).
        elif command[0] in HBNBCommand.project_classes:
            class_name = command[0]
            id_1 = command[1].split("(")
            id_2 = id_1[1].split(")")

            if command[1].startswith("show(") and command[1].endswith(")"):
                command_1 = "{} {}".format(class_name, id_2[0])
                self.do_show(command_1)

            elif command[1].startswith("destroy(") and command[
                    1].endswith(")"):
                command_1 = "{} {}".format(class_name, id_2[0])
                self.do_destroy(command_1)

            elif command[1].startswith("update(") and command[
                    1].endswith(")"):
                id_2 = id_2[0].split(",")
                command_1 = f"{class_name} {id_2[0]}{id_2[1]}{id_2[2]}"
                print(command_1)
                self.do_update(command_1)

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the ID.
        Usage: create <class name>"""
        instance_obj = line.split(" ")
        if not line:
            print("** class name missing **")

        else:
            if instance_obj[0] not in HBNBCommand.project_classes:
                print("** class doesn't exist **")

            else:
                if instance_obj[0] == "BaseModel":
                    new_instance = BaseModel()

                elif instance_obj[0] == "User":
                    new_instance = User()

                elif instance_obj[0] == "City":
                    new_instance = City()

                elif instance_obj[0] == "State":
                    new_instance = State()

                elif instance_obj[0] == "Place":
                    new_instance = Place()

                elif instance_obj[0] == "Review":
                    new_instance = Review()

                elif instance_obj[0] == "Amenity":
                    new_instance = Amenity()

                # save the instance to json file
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
            class name and id"""
        all_objec = storage.all()
        instance_obj = line.split(" ")
        if not line:
            print("** class name missing **")
        elif instance_obj[0] not in HBNBCommand.project_classes:
            print("** class doesn't exist **")
        elif len(instance_obj) < 2:
            print("** instance id missing **")
        else:
            # Removing quotes if present in the ID
            # Checking if the ID starts and ends with quotes
            if instance_obj[1].startswith('"') and instance_obj[
                    1].endswith('"'):
                # Remove the quotes
                instance_obj[1] = instance_obj[1][1:-1]
            # Creating a unique identifier for the instance
            class_id = instance_obj[0] + "." + instance_obj[1]

            # Checking if the instance exists in the storage
            if class_id not in all_objec.keys():
                print("** no instance found **")
            else:
                print(all_objec[class_id])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id> or <class name>.destroy(<id>)
        """
        all_objec = storage.all()
        instance_obj = line.split(" ")
        if not line:
            print("** class name missing **")
        elif instance_obj[0] not in HBNBCommand.project_classes:
            print("** class doesn't exist **")
        elif len(instance_obj) < 2:
            print("** instance id missing **")
        else:
            if instance_obj[1].startswith('"') and instance_obj[
                    1].endwith('"'):

                instance_obj[1] = instance_obj[1][1:-1]
            class_id = instance_obj[0] + "." + instance_obj[1]

            if class_id not in all_objec.keys():
                print("** no instance found **")
            else:
                del all_objec[class_id]
                storage.save()

    def do_all(self, line):
        """
        Retrieves all instances of a class. Usage: all or all <class name>
        or <class name>.all().
        """
        all_object = storage.all()
        list = []

        if line:
            if line not in HBNBCommand.project_classes:
                print("** class doesn't exist **")
            else:
                for key, value in all_object.items():
                    if value.__class__.__name__ == line:
                        list.append(str(value))
                print(list)
        else:
            for key, value in all_object.items():
                list.append(str(value))
            print(list)

    def do_update(self, line):
        """
            Updates an instance based on the class name and
            id by adding or updating attribute
        """
        all_objects = storage.all()
        if not line:
            print("** class name missing **")
        else:
            if "\"" in line:
                line = line.replace("\"", "")

            instance_obj = line.split(" ")
            if instance_obj[0] not in HBNBCommand.project_classes:
                print("** class doesn't exist **")

            else:
                if len(instance_obj) < 2:
                    print("** instance id missing **")

                else:
                    class_id = instance_obj[0] + "." + instance_obj[1]

                    if class_id not in all_objects.keys():
                        print("** no instance found **")

                    else:

                        if len(instance_obj) < 3:
                            print("** attribute name missing **")

                        else:

                            if len(instance_obj) < 4:
                                print("** value missing **")

                            else:

                                for key, value in all_objects.items():
                                    name = value.__class__.__name__
                                    id_1 = value.id
                                    di_1 = value.__dict__
                                    if id_1 == instance_obj[
                                            1] and name == instance_obj[0]:
                                        if instance_obj[2] in di_1.keys():
                                            cast = type(di_1[instance_obj[2]])
                                            di_1.update({instance_obj[
                                                2]: cast(instance_obj[3])})
                                        else:
                                            di_1.update({instance_obj[
                                                2]: instance_obj[3]})
                                        break
                                storage.save()

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """ Handle the end-of-file condition (Ctrl+D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
