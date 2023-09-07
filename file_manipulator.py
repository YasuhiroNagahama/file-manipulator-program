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
        self.contents = ''

    def copy(self):
        print('copy')

    def reverse(self):
        print('reverse')

    def help(self):
        path_name = 'help.txt'

        with open(path_name) as f:
            self.contents = f.read()

        print(self.contents)

    def duplicate_contents(self):
        # with open(self.input_path, 'r') as f:
        #   self.contents = f.read()

        # with open(self.input_path, 'w') as f:
        #   for i in self.iterations:
        #       f.write(self.contents + self.contents)

        print('duplicate_contents')

    def replace_string(self):
        print('replace_string')

    # コマンドが正しい長さか確認してブーリアン値で返すメソッド
    def is_valid_length(self):
        if self.args[1] == 'help':
            return len(self.args == 2)
        elif self.args[1] == 'replace-string':
            return len(self.args) == 5

        return len(self.args) == 4

    # コマンドがcommand_mapに存在するかブーリアン値で返すメソッド
    def is_valid_command(self):
        return self.command in self.command_map

    # ファイルパスが正しいかブーリアン値で返すメソッド
    def is_valid_path(self, file_path):
        return os.path.isfile(file_path)

    # 現在メンバ変数に保存されているデータが正しいか確認するメソッド
    def is_valid_data_type(self):
        if(self.command == 'copy' or self.command == 'reverse'):
           if self.is_valid_path(self.input_path) and self.is_valid_path(self.output_path):
               return True
           else:
               print("input_path、または、output_pathのパスが正しくありません。")
               return False
        elif(self.command == 'duplicate-contents'):
          try:
            if not self.is_valid_path(self.input_path):
                return False
            
            n = int(self.iterations)
            if n > 0:
                return True
            else:
                print('エラー: n を0より大きい正の整数にしてください。')
                return False
          except ValueError:
            print('エラー: n の値が数値に変換できない文字になっています。')
            return False

    # 入力されたコマンドから、必要な情報をメンバ変数に保存するメソッド
    def set_data(self):
        self.input_path = self.args[2]

        if(self.command == 'copy' or self.command == 'reverse'):
            self.output_path = self.args[3]
        elif(self.command == 'duplicate-contents'):
            self.iterations = self.args[3]
        elif(self.command == 'replace_string'):
            self.needle = self.args[3]
            self.new_string = self.args[4]

    def analyze_command(self):
        if self.is_valid_command() and self.is_valid_length():
            self.set_data()
            if self.is_valid_data_type():
                self.command_map[self.command]()
        else:
            print('エラー: 正しい入力形式でない、もしくは、存在しないコマンドです。')

    # 入力されたコマンドを解析するメソッド
    def analyze_input(self):
        self.args = sys.argv

        if len(self.args) <= 1:
            print('エラー: コマンドを入力してください。')
            return

        self.command = self.args[1]
        self.analyze_command()


file_manipulator_program = FileManipulator()
file_manipulator_program.analyze_input()