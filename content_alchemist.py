import sys
# utf-8のみをサポートするため、エンコードを指定してファイルを開く
def reverse_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content[::-1])
    except UnicodeDecodeError:
        print("エラー: 入力ファイルのエンコーディングはUTF-8である必要があります。エンコードをUTF-8に変更してください。")
        sys.exit(1)
    except Exception as e:
        print(f"ファイルを逆順にする際にエラーが発生しました: {e}")
        sys.exit(1)

def copy_file(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except UnicodeDecodeError:
        print("エラー: 入力ファイルのエンコーディングはUTF-8である必要があります。エンコードをUTF-8に変更してください。")
        sys.exit(1)
    except Exception as e:
        print(f"ファイルをコピーする際にエラーが発生しました: {e}")
        sys.exit(1)

def duplicate_contents(input_path, n):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        with open(input_path, 'w', encoding='utf-8') as file:
            file.write(content * n)
    except UnicodeDecodeError:
        print("エラー: 入力ファイルのエンコーディングはUTF-8である必要があります。エンコードをUTF-8に変更してください。")
        sys.exit(1)
    except Exception as e:
        print(f"内容を複製する際にエラーが発生しました: {e}")
        sys.exit(1)

def replace_string(input_path, needle, new_string):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()
        with open(input_path, 'w', encoding='utf-8') as file:
            file.write(content.replace(needle, new_string))
    except UnicodeDecodeError:
        print("エラー: 入力ファイルのエンコーディングはUTF-8である必要があります。エンコードをUTF-8に変更してください。")
        sys.exit(1)
    except Exception as e:
        print(f"文字列を置き換える際にエラーが発生しました: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("使用法: python content_alchemist.py <コマンド> <引数>")
        sys.exit(1)
    
    command = sys.argv[1]
    if command == "reverse":
        if len(sys.argv) != 4:
            print("使用法: reverse <入力パス> <出力パス>")
            sys.exit(1)
        reverse_file(sys.argv[2], sys.argv[3])
    elif command == "copy":
        if len(sys.argv) != 4:
            print("使用法: copy <入力パス> <出力パス>")
            sys.exit(1)
        copy_file(sys.argv[2], sys.argv[3])
    elif command == "duplicate-contents":
        if len(sys.argv) != 4:
            print("使用法: duplicate-contents <入力パス> <n>")
            sys.exit(1)
        duplicate_contents(sys.argv[2], int(sys.argv[3]))
    elif command == "replace-string":
        if len(sys.argv) != 5:
            print("使用法: replace-string <入力パス> <検索文字列> <新しい文字列>")
            sys.exit(1)
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(f"未知のコマンド: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
