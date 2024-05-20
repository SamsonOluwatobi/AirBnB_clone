#!/usr/bin/env python3
import cmd



"""
Module to define the HBNB console class.

This module defines a class, HBNBCommand, which inherits from the
cmd.Cmd class. This class is used to define the commands available in
the HBNB console.

"""

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

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exiting using EOF.
        """
        return True

    def emptyline(self):
        "Do nothing on empty line"
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
