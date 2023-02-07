#!/usr/bin/python3
'''
the entry point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    command interpreter for AirBnB project with commands to be used
    '''

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
