#!/usr/bin/python3
'''
the entry point of the command interpreter
'''
import cmd
import re


class HBNBCommand(cmd.Cmd):
    '''
    command interpreter for AirBnB project with commands to be used
    '''
    prompt = "(hbnbtest)"
    def precmd(self, line):
        newline = ""
        if line:
            print(line)
            pattern = re.compile(r"^[a-zA-Z]+\.[a-z]+\(.*\)")
            if pattern.search(line):
                newline = line.replace(".", " ").replace("(", "").replace(")", "").replace("\"", " ")
            else:
                print("no match")
        print(newline)
        return newline
    def do_User(self, line):
        print(line)

    def do_EOF(self, line):
        '''end of file marker used to exit the program
        '''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def emptyline(self):
        '''e'''
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
