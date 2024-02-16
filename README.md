# ContentAlchemist
概要
--

ContentAlchemistは、ファイルの内容を逆順にしたり、ファイルのコピーを作成したり、ファイルの内容を複製したり、特定の文字列を新しい文字列に置き換えたりする機能を提供するコマンドラインツールです。このユーティリティはPythonで書かれており、簡単にファイル操作を自動化するための便利な方法を提供します。

特徴
--

*   ファイルの内容を逆順にして新しいファイルに保存
*   指定されたファイルのコピーを作成
*   ファイルの内容を指定された回数だけ複製
*   ファイル内の特定の文字列を新しい文字列で置き換え

使用方法
----

このツールはコマンドラインから実行され、以下のコマンドをサポートしています：

### reverse
```bash
python3 content_alchemist.py reverse <入力パス> <出力パス>
```

入力パスにあるファイルの内容を逆にして、出力パスに保存します。

### copy

```bash
python3 content_alchemist.py copy <入力パス> <出力パス>
```

入力パスにあるファイルをコピーして、出力パスに保存します。

### duplicate-contents

```bash
python3 content_alchemist.py duplicate-contents <入力パス> <n>
```

入力パスにあるファイルの内容をn回複製して、同じファイルに保存します。

### replace-string

```bash
python3 content_alchemist.py replace-string <入力パス> <検索文字列> <新しい文字列>
```

入力パスにあるファイル内の特定の文字列を新しい文字列で置き換えます。

必要条件
----

- Python 3.x

インストール方法
----

このプログラムは追加のインストールなしでPython 3.xがあれば実行可能です。ただし、Pythonがインストールされていない場合は、[Pythonの公式ウェブサイト](https://www.python.org/downloads/)からインストールしてください。

実行方法
----
ターミナルまたはコマンドプロンプトで以下のコマンドを実行します。

```bash
python3 content_alchemist.py <コマンド> <引数>
```
