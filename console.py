#!/usr/bin/env python3
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        "Exiting using EOF"
        return True

    def do_help(self, arg):
        "getting information on each keyword"
        cmd.Cmd.do_help(self, arg)




if __name__ == "__main__":
    HBNBCommand().cmdloop()
