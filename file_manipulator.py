# openメソッドでファイルを読み込む
# closeメソッドでファイルを閉じる（ファイルを閉じることにより、OSはファイル記述子を解放し、ファイルの更新を確定し、他のプロセスで使用できるようにします）


pathname = 'test.txt'
file = open(pathname)
contents = file.read()
file.close()