from fileHandler import printClass
from cmd import Cmd


class fileInput(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "

    def do_input(self, the_string):
        """
        Syntax: input [option] the_string
        Writes plantUML to a file
        :param [option] : % (represents leading four spaces)
        :param the_string : a string representing one line of a plantUML file
        :return: None
        """
        with open('classDiagram.txt', 'a') as output:
            if the_string[0:1] == '%':
                output.write('   ' + the_string[1:] + '\n')
            else:
                output.write(the_string + '\n')

    def do_printClass(self, line):
        this = printClass('classDiagram.txt')
        this.outputClasses()

    def do_quit(self, line):
        print("Quitting ......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from python CMD', ':return: True']))

    do_q = do_quit


if __name__ == "__main__":
    fileInput().cmdloop()
