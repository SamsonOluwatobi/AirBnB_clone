#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A class that inherits from the cmd.Cmd class. This class is used to define
    the commands available in the HBNB console.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): Unused argument

        Returns:
            bool: True to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exiting using EOF.

        Args:
            arg (str): Unused argument

        Returns:
            bool: True to exit the program
        """
        return True

    def do_help(self, arg):
        """
        Getting information on each keyword.

        Args:
            arg (str): The keyword to get information on

        Returns:
            None
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        "Do nothing on empty line"
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
