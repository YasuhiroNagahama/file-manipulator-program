import sys


class FileManipulator:
    def __init__(self):
        self.input_path = ''
        self.output_path = ''
        self.iterations = 0
        self.new_string = ''
        self.command = ''
        self.commands = ['copy', 'reverse',
                         'duplicate-contents', 'replace-string']

    # コマンドの説明をコンソールに出力するメソッド
    def help():
        path_name = 'help.txt'
        contents = ''

        with open(path_name) as f:
            contents = f.read()

        print(contents)

    def reserve():
        print()

    # コマンドが正しい長さか確認してブーリアン値で返すメソッド
    def is_valid_length(self, args):
        if args[1] == 'replace-string' and len(args) == 5:
            return True

        return len(args) == 4

    # コマンドがcommandsに存在するかブーリアン値で返すメソッド
    def is_valid_command(self, command):
        return command in self.commands

    # この関数に来た時点でインデックスが存在しないことはないはず
    def execute_command(self):
        if self.command == 'copy':
            print('reverse')
        elif self.command == 'reverse':
            print('copy')
        elif self.command == 'duplicate-contents':
            print('duplicate-contents')
        elif self.command == 'replace-string':
            print('replace-string')

    # 入力されたコマンドを解析するメソッド
    def parseInput(self):
        args = sys.argv

        if len(args) <= 1:
            return print('正しい入力形式ではありません。')

        self.command = args[1]

        if (self.is_valid_command(self.command) and self.is_valid_length(args)):
            self.execute_command()
        else:
            print('正しい入力形式でない、もしくは、存在しないコマンドです。')


file_manipulator_program = FileManipulator()
file_manipulator_program.parseInput()
