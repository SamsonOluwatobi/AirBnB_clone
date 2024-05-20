#!/usr/bin/env python3
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        "Exiting the console"
        return True

    def do_EOF(self, arg):
        "Exiting using EOF"
        return True

    def do_help(self, arg):
        "getting information on each keyword"
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        "Do nothing on empty line"
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()