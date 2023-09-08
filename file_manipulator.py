import sys
import os

from abc import ABC


class CommandInterface(ABC):
    def set_data(self):
        pass

    def is_valid_length(self):
        pass

    def is_valid_path(self, file_path):
        pass


class Help:
    def __init__(self, args: list):
        self.valid_length: int = 2
        self.args: list = args

    def is_valid_length(self):
        return len(self.args) == self.valid_length

    def run_command(self):
        if self.is_valid_length():
            path_name = 'help.txt'
            contents = ''

            with open(path_name, "r") as f:
                contents = f.read()

            print(contents)
        else:
            print('コマンドの入力形式が間違っています。')


class Reverse(CommandInterface):
    def __init__(self, args: list):
        self.valid_length: int = 4
        self.args: list = args
        self.data_format: str = ''
        self.input_path: str = ''
        self.output_path: str = ''

    def is_valid_length(self):
        return len(self.args) == self.valid_length

    def set_path(self):
        self.input_path = self.args[2]
        self.output_path = self.args[3]

    def is_exist_path(self, path):
        return os.path.exists(path)

    def is_file_path(self, file_path):
        return os.path.isfile(file_path)

    def run_command(self):
        if not self.is_valid_length():
            print('コマンドの入力形式が間違っています。')
            return

        self.set_path()

        if not self.is_exist_path(self.input_path):
            print(self.input_path + 'は存在しません。')
            return
        if not self.is_exist_path(self.output_path):
            print(self.output_path + 'は存在しません。')
            return
        

        contents = ''

        with open(self.input_path, "r") as f:
            file_contents = f.read()
            contents = file_contents[::-1]

        # 上書きしてもよいか確認する条件分岐
        # フォルダの場合どうするか？
        with open(self.output_path, "w") as f:
            f.write(contents)

        print(contents)


class Copy:
    def __init__(self, args: list):
        self.args: list = args
        self.input_path: str = ''
        self.output_path: str = ''

    def __str__(self):
        print('copy')


class DuplicateContents:
    def __init__(self, args: list):
        self.args: list = args
        self.input_path: str = ''
        self.iterations = 0

    def __str__(self):
        print('duplicate contents')


class ReplaceString:
    def __init__(self, args: list):
        self.args: list = args
        self.needle = ''
        self.new_string = ''

    def __str__(self):
        print('replace string')


class FileManipulator():
    def __init__(self):
        self.args: list = []
        self.command: str = ''
        self.command_class_map: map = {
            'help': Help,
            'copy': Copy,
            'reverse': Reverse,
            'duplicate-contents': DuplicateContents,
            'replace-string': ReplaceString
        }

    # 有効なコマンドかどうかをブーリアン値で返すメソッド
    def is_exist_command(self):
        return self.command in self.command_class_map

    # 入力されたコマンドを解析するメソッド
    def analyze_input(self):
        self.args = sys.argv

        if len(self.args) <= 1:
            print('エラー: コマンドを入力してください。')
            return

        self.command = self.args[1]

        if not self.is_exist_command():
            print('エラー: 存在しないコマンドです。')
            return

        command_program: object = self.command_class_map[self.command](
            self.args)
        command_program.run_command()


file_manipulator_program = FileManipulator()
file_manipulator_program.analyze_input()
