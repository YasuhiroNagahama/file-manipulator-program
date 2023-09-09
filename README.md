# Name

**File Manipulator Program**

# Explain

OSとやりとりするプロジェクトです。file_manipulator.pyファイルには、ファイルを操作するためのコマンドが含まれています。以下がコマンドです。

* **helpコマンド** -- File Manipulator Program のコマンドの使い方が表示されます。

* **reverseコマンド** -- inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。

* **copyコマンド** -- inputpath にあるファイルのコピーを作成し、outputpath として保存します。

* **duplicate-contentsコマンド** -- inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。

* **replace-stringコマンド** -- inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

# Features

* オブジェクト指向プログラミングを行いました。
* すべてのクラス内で同じ処理をするコードをメソッドではなく、関数としてまとめました。
* 間違った形式でコマンドが入力された場合に、エラー文が出るようにしました。（すべてのエラーをとりきれるかはわからない）

# Author

* 作成者 YasuhiroNagahama
* E-mail fnifhubi85h29bddi@gmail.com
