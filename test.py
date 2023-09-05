# openメソッドでファイルを読み込む
# readメソッドでファイルの内容を読み込む
# closeメソッドでファイルを閉じる（ファイルを閉じることにより、OSはファイル記述子を解放し、ファイルの更新を確定し、他のプロセスで使用できるようにします）
pathname = 'test.txt'
contents = ''

# f → 読み込み後のファイル
with open(pathname) as f:
  # contentsにf(test.txt)の内容が代入される
    contents = f.read()
    
# 書き込みモード(w)でファイルを開く
with open(pathname, 'w') as f:
    # ファイルに書き込む
    f.write(contents + "\nAppending more text to this file!")