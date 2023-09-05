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
    
    def is_valid_length(self, args):
      if args[1] == 'replace-string' and len(args) == 5:
          return True
      
      return len(args) == 4
    
    def is_valid_command(self, command):
      return command in self.commands

    def parseInput(self):
      args = sys.argv

      if len(args) <= 1:
        return print('正しい入力形式ではありません。')

      if(self.is_valid_command(args[1]) and self.is_valid_length(args)):
        print(args[1])
      else:
        print('正しい入力形式でない、もしくは、存在しないコマンドです。')

file_manipurator_program = FileManipulator()
file_manipurator_program.parseInput()


