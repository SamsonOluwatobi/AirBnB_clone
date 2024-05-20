#!/usr/bin/env python3
"""
Module to define the HBNB console class.

This module defines a class, HBNBCommand, which inherits from the
cmd.Cmd class. This class is used to define the commands available in
the HBNB console.

"""
#!/usr/bin/env python3
import json
import os
from cmd import Cmd
from models.base_model import BaseModel
from models.file_storage import FileStorage

storage = FileStorage()
storage.reload()


class HBNBCommand(Cmd):
    """
    A class that inherits from the cmd.Cmd class. This class is used to define
    the commands available in the HBNB console.

    Attributes:
        prompt (str): The prompt string used in the console.

    Methods:
        do_create -- Command to create a new instance of a model
        do_show -- Command to display an instance of a model
        do_destroy -- Command to delete an instance of a model
        do_all -- Command to display all instances of a model or all models
        do_update -- Command to update an attribute of an instance of a model
    """

    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Create a new instance of a model and save it to the JSON file.

        Args:
            arg (str): The class name of the model to create.

        Returns:
            None
        """
        args = arg.split()
        if len(args) == 0:
            print("class name missing")
        elif not hasattr(BaseModel, args[0]):
            print("class doesn't exist")
        else:
            new_instance = getattr(BaseModel, args[0])()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Display an instance of a model based on class name and ID.

        Args:
            arg (str): The class name and ID of the instance to display.

        Returns:
            None
        """
        args = arg.split()
        if len(args) == 0:
            print("class name missing")
        elif len(args) == 1:
            print("instance id missing")
        elif not hasattr(BaseModel, args[0]):
            print("class doesn't exist")
        elif len(args) > 2:
            print("too much arguments")
        else:
            class_name = args[0]
            instance_id = args[1]
            instance = storage.get_instance(class_name, instance_id)
            if instance:
                print(instance)
            else:
                print("no instance found")

    def do_destroy(self, arg):
        """
        Delete an instance of a model based on class name and ID.

        Args:
            arg (str): The class name and ID of the instance to delete.

        Returns:
            None
        """
        args = arg.split()
        if len(args) == 0:
            print("class name missing")
        elif len(args) == 1:
            print("instance id missing")
        elif not hasattr(BaseModel, args[0]):
            print("class doesn't exist")
        elif len(args) > 2:
            print("too much arguments")
        else:
            class_name = args[0]
            instance_id = args[1]
            instance = storage.get_instance(class_name, instance_id)
            if instance:
                storage.delete_instance(instance)
                storage.save()
            else:
                print("no instance found")

    def do_all(self, arg):
        """
        Display all instances of a model or all models.

        Args:
            arg (str): The class name or empty string.

        Returns:
            None
        """
        args = arg.split()
        if len(args) > 1:
            print("too much arguments")
        elif len(args) == 1:
            class_name = args[0]
            if hasattr(BaseModel, class_name):
                instances = storage.get_instances(class_name)
                if instances:
                    for instance in instances:
                        print(instance)
                else:
                    print("no instances found")
            else:
                print("class doesn't exist")
        else:
            instances = storage.get_all_instances()
            if instances:
                for instance in instances:
                    print(instance)
            else:
                print("no instances found")

    def do_update(self, arg):
        """
        Update an attribute of an instance of a model.

        Args:
            arg (str): The class name, ID, attribute name, and new value.

        Returns:
            None
        """
        args = arg.split()
        if len(args) < 4:
            if len(args) == 0:
                print("class name missing")
            elif len(args) == 1:
                print("instance id missing")
            elif len(args) == 2:
                print("attribute name missing")
            else:
                print("value missing")
        elif len(args) > 5:
            print("too much arguments")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            if not hasattr(BaseModel, class_name):
                print("class doesn't exist")
            elif not storage.has_instance(class_name, instance_id):
                print("no instance found")
            elif attribute_name in ["id", "created_at", "updated_at"]:
                print("can't update id, created_at or updated_at")
            else:
                instance = storage.get_instance(class_name, instance_id)
                if instance:
                    setattr(instance, attribute_name, self._cast_value(attribute_value))
                    storage.save()
                else:
                    print("no instance found")

    def _cast_value(self, value):
        """
        Cast a string value to the appropriate type.

        Args:
            value (str): The string value to cast.

        Returns:
            The casted value.
        """
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exiting using EOF"""
        return True

    def emptyline(self):
        "Do nothing on empty line"
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
