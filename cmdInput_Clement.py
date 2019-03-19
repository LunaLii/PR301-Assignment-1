from fileHandler import printClass
from cmd import Cmd
import os


class fileInput(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.the_file = "classDiagram.txt"

    def do_file(self, the_file):
        """
        Syntax: file the_file
        Sets the file to write to
        :param the_file: filename you want to write to (no quotations)
        :return: None
        """

        if the_file:
            self.the_file = the_file
        print('You are now writing to ' + self.the_file)

    def do_input(self, the_input):
        """
        Syntax: input [option] the_string
        Writes plantUML to a file
        :param [option]: % (represents leading four spaces)
        :param the_input: a string representing one line of a plantUML file
        For an empty space, just type input then press enter
        :return: None
        """
        with open(self.the_file, 'a') as output:
            if the_input[0:1] == '%':
                output.write('   ' + the_input[1:] + '\n')
            else:
                output.write(the_input + '\n')

    def do_writeCode(self, line):
        """
        Syntax: writeCode
        Creates new files and writes class to each
        :return: None
        """
        if os.stat(self.the_file).st_size != 0:
            printClass(self.the_file).outputClasses()
        else:
            print("Error! Writing to empty file!")

    def do_quit(self, line):
        print("exiting ......")
        return True

    def help_exit(self):
        print("\n".join(['Quit from python CMD', ':return: True']))

    do_q = do_quit


if __name__ == "__main__":
    fileInput().cmdloop()
