import sys
import os


class FileManipulator:
    def __init__(self):
        self.args = []
        self.input_path = ''
        self.output_path = ''
        self.iterations = 0
        self.needle = ''
        self.new_string = ''
        self.command = ''
        self.command_map = {
            'copy': self.copy,
            'help': self.help,
            'reverse': self.reverse,
            'duplicate-contents': self.duplicate_contents,
            'replace-string': self.replace_string
        }

    def copy(self):
        print()

    def reverse(self):
        print()

    # コマンドの説明をコンソールに出力するメソッド
    def help(self):
        path_name = 'help.txt'
        contents = ''

        with open(path_name) as f:
            contents = f.read()

        print(contents)

    def duplicate_contents(self):
        print()

    def replace_string(self):
        print()

    # コマンドが正しい長さか確認してブーリアン値で返すメソッド
    def is_valid_length(self):
        if self.args[1] == 'replace-string':
            return len(self.args) == 5

        return len(self.args) == 4

    # コマンドがcommand_mapに存在するかブーリアン値で返すメソッド
    def is_valid_command(self):
        return self.command in self.command_map

    def is_valid_path(self, file_path):
        return os.path.isfile(file_path)

    def temp(self):
        self.input_path = self.args[2]

        if(self.command == 'copy' or self.command == 'reverse'):
            self.output_path = self.args[3]
        elif(self.command == 'duplicate-contents'):
            # この場合はself.argsを数値型に変えるので、後ほど
            self.iterations = self.args[3]
        elif(self.command == 'replace_string'):
            self.needle = self.args[3]
            self.new_string = self.args[4]

    def parse_command(self):
        if (self.args[1] == 'help'):
            self.help()
        elif self.is_valid_command() and self.is_valid_length():
            self.command_map[self.command]()
        else:
            print('正しい入力形式でない、もしくは、存在しないコマンドです。')

    # 入力されたコマンドを解析するメソッド
    def parse_input(self):
        self.args = sys.argv

        # python file-manipulator-programを除外
        if len(self.args) <= 1:
            print('コマンドを入力してください。')
            return

        self.command = self.args[1]
        self.temp()
        self.parse_command()


file_manipulator_program = FileManipulator()
file_manipulator_program.parse_input()
