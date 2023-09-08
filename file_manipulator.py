import sys
import os

from abc import ABC


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
            print('エラー: コマンドの入力形式が間違っています。')


class Reverse:
    def __init__(self, args: list):
        self.valid_length: int = 4
        self.args: list = args
        self.input_path: str = ''
        self.output_path: str = ''

    def is_valid_length(self):
        return len(self.args) == self.valid_length

    def is_file(self, path):
        return os.path.isfile(path)

    def set_path(self):
        self.input_path = self.args[2]
        self.output_path = self.args[3]

    def is_valid_command(self):
        if not self.is_valid_length():
            print('\nエラー: コマンドの入力形式が間違っています。')
            return False

        self.set_path()

        if not self.is_file(self.input_path):
            print('\nエラー: ' + self.input_path + ' は存在しないか、ファイルではありません。')
            return False
        if not self.is_file(self.output_path):
            print('\nエラー: ' + self.output_path + ' は存在しないか、ファイルではありません。')
            return False

        return True

    def is_overwrite_allowed(self):
        overwrite_permission = input('\n上書きを許可しますか？ (y/n): ')

        while overwrite_permission not in ["y", "n", 'Y', 'N']:
            print("\nエラー: 無効な入力です。'y' または 'n' を入力してください。")
            overwrite_permission = input('\n上書きを許可しますか？ (y/n): ')

        if overwrite_permission == 'n' or overwrite_permission == 'N':
            print('\n処理を中止しました。')
            return False

        return True

    def run_command(self):
        if not self.is_valid_command() or not self.is_overwrite_allowed():
            return

        contents = ''

        with open(self.input_path, "r") as f:
            file_contents = f.read()
            contents = file_contents[::-1]

        with open(self.output_path, "w") as f:
            f.write(contents)

        print('\n処理を完了しました。')


class Copy:
    def __init__(self, args: list):
        self.valid_length: int = 4
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

    def is_exist_command(self):
        return self.command in self.command_class_map

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
