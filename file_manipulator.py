import sys
import os


def is_overwrite_allowed() -> bool:
    overwrite_permission = input(
        '\ninput_pathもしくはoutput_pathのファイルの内容が上書きされます。許可しますか？ (y/n): ')

    while overwrite_permission not in ["y", "n", 'Y', 'N']:
        print("\nエラー: 無効な入力です。'y' または 'n' を入力してください。")
        overwrite_permission = input(
            '\ninput_pathもしくはoutput_pathのファイルの内容が上書きされます。許可しますか？ (y/n): ')

    if overwrite_permission == 'n' or overwrite_permission == 'N':
        print('\n処理を中止しました。')
        return False

    return True


def is_file(path: str) -> bool:
    return os.path.isfile(path)


class Help:
    def run_command(self):
        path_name: str = 'help.txt'
        contents: str = ''

        with open(path_name, "r") as f:
            contents = f.read()
            print(contents)


class Reverse:
    def __init__(self, args: list):
        self.args: list = args
        self.input_path: str = ''
        self.output_path: str = ''

    def set_path(self):
        self.input_path = self.args[2]
        self.output_path = self.args[3]

    def is_valid_command(self) -> bool:
        if not is_file(self.input_path):
            print('\nエラー: ' + self.input_path + ' は存在しないか、ファイルではありません。')
            return False
        if not is_file(self.output_path):
            print('\nエラー: ' + self.output_path + ' は存在しないか、ファイルではありません。')
            return False

        return True

    def run_command(self):
        self.set_path()
        if not self.is_valid_command() or not is_overwrite_allowed():
            return

        original_contents: str = ''
        reverse_contents: str = ''

        with open(self.input_path, "r") as f:
            original_contents = f.read()
            reverse_contents = original_contents[::-1]

        with open(self.output_path, "w") as f:
            f.write(reverse_contents)


class Copy:
    def __init__(self, args: list):
        self.args: list = args
        self.input_path: str = ''
        self.output_path: str = ''

    def set_path(self):
        self.input_path = self.args[2]
        self.output_path = self.args[3]

    def is_valid_command(self) -> bool:
        if not is_file(self.input_path):
            print('\nエラー: ' + self.input_path + ' は存在しないか、ファイルではありません。')
            return False
        if not is_file(self.output_path):
            print('\nエラー: ' + self.output_path + ' は存在しないか、ファイルではありません。')
            return False

        return True

    def run_command(self):
        self.set_path()
        if not self.is_valid_command() or not is_overwrite_allowed():
            return

        original_contents = ''

        with open(self.input_path, "r") as f:
            original_contents = f.read()

        with open(self.output_path, "w") as f:
            f.write(original_contents)


class DuplicateContents:
    def __init__(self, args: list):
        self.args: list = args
        self.input_path: str = ''
        self.iterations = 0

    def set_path(self):
        self.input_path = self.args[2]

    def set_iterations(self):
        self.iterations = int(self.args[3])

    def is_valid_iterations(self) -> bool:
        try:
            num = int(self.args[3])
            if num > 1:
                return True
            else:
                print('2以上の数値を指定してください。')
                return False
        except ValueError:
            print("エラー: 文字列は整数に変換できません。")
            return False

    def is_valid_command(self) -> bool:
        if not is_file(self.input_path):
            print('\nエラー: ' + self.input_path + ' は存在しないか、ファイルではありません。')
            return False

        if not self.is_valid_iterations():
            return False

        return True

    def run_command(self):
        self.set_path()
        if not self.is_valid_command() or not is_overwrite_allowed():
            return

        self.set_iterations()

        original_contents = ''
        repeated_contents = ''

        with open(self.input_path, "r") as f:
            original_contents = f.read()

        with open(self.input_path, "w") as f:
            for i in range(0, self.iterations):
                repeated_contents += original_contents
            f.write(repeated_contents)


class ReplaceString:
    def __init__(self, args: list):
        self.args: list = args
        self.input_path = ''
        self.needle = ''
        self.new_string = ''

    def set_path(self):
        self.input_path = self.args[2]

    def set_needle(self):
        self.needle = self.args[3]

    def set_new_string(self):
        self.new_string = self.args[4]

    def is_valid_command(self) -> bool:
        if not is_file(self.input_path):
            print('\nエラー: ' + self.input_path + ' は存在しないか、ファイルではありません。')
            return False

        return True

    def run_command(self):
        self.set_path()
        if not self.is_valid_command() or not is_overwrite_allowed():
            return

        self.set_needle()
        self.set_new_string()

        original_contents = ''
        new_contents = ''

        with open(self.input_path, "r") as f:
            original_contents = f.read()
            new_contents = original_contents.replace(
                self.needle, self.new_string)

        with open(self.input_path, "w") as f:
            f.write(new_contents)


class FileManipulator():
    def __init__(self):
        self.args: list = []
        self.command: str = ''
        self.command_class_map: dict = {
            'help': Help,
            'copy': Copy,
            'reverse': Reverse,
            'duplicate-contents': DuplicateContents,
            'replace-string': ReplaceString
        }
        self.command_length_map: dict = {
            'help': 2,
            'copy': 4,
            'reverse': 4,
            'duplicate-contents': 4,
            'replace-string': 5
        }

    def is_exist_command(self) -> bool:
        return self.command in self.command_class_map

    def is_valid_length(self) -> bool:
        return len(self.args) == self.command_length_map[self.command]

    def is_valid_command(self) -> bool:
        if len(self.args) <= 1:
            print('\nエラー: コマンドを入力してください。')
            return False

        self.command = self.args[1]

        if not self.is_exist_command():
            print('\nエラー: 存在しないコマンドです。')
            return False
        if not self.is_valid_length():
            print('\nエラー: コマンドの入力形式が間違っています。')
            return False

        return True

    def analyze_input(self):
        self.args: list = sys.argv
        command_program: object

        if self.is_valid_command():
            if self.command == 'help':
                command_program = self.command_class_map[self.command]()
            else:
                command_program = self.command_class_map[self.command](
                    self.args)

            command_program.run_command()


file_manipulator_program = FileManipulator()
file_manipulator_program.analyze_input()
