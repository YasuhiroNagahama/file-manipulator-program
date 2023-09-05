import sys

class FileManipulator:
    def __init__(self):
        self.inputpath = ''
        self.outputpath = ''
        self.commands = ['copy', 'reverse', 'duplicate-contents', 'replace-string']

    def description():
      path_name = 'description.txt'
      contents = ''

      with open(path_name) as f:
        contents = f.read()

      print(contents)

    def reserve():
      input("File Manipulator Program >> ")

    def lengthCheck(self, args):
       return len(args) == 3 or len(args) == 4
    
    def commandCheck(self, command):
       return command in self.commands

    def parseInput(self):
      args = sys.argv

      if(self.lengthCheck(args) and self.commandCheck(args[1])):
         print(args[1])
      else:
         print('存在しないコマンドです。')

file_manipurator_program = FileManipulator()
file_manipurator_program.parseInput()


