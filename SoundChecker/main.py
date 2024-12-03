import os
import wave


def count_files_in_folder(folder_path):
    """
    指定したフォルダ内のファイル数を数える関数
    """
    if not os.path.isdir(folder_path):
        raise ValueError(f"指定したパスはフォルダではありません: {folder_path}")

    file_count = 0
    for root, _, files in os.walk(folder_path):
        file_count += len(files)

    return file_count


def check_file_format(folder_path):
    """
    ファイル形式の一致をチェックする
    """
    print("\nファイル形式のチェックを開始します...")
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".wav"):
                file_path = os.path.join(root, file)
                try:
                    # WAVファイルとして開けるか確認
                    with wave.open(file_path, 'rb') as wav_file:
                        wav_file.getnchannels()  # チャネル情報を取得（有効性の確認）
                except wave.Error:
                    print(f"エラー: {file} はWAV形式ではありません。")
                except Exception as e:
                    print(f"エラー: {file} のチェック中に予期しないエラーが発生しました: {e}")


def check_format_consistency(folder_path):
    print("フォーマットの整合性をチェック中...")


def check_naming_rules(folder_path):
    print("命名規則のチェックを実行中...")


def check_volume_level(folder_path):
    print("音量レベルのチェックを実行中...")


def check_silence(folder_path):
    print("無音部分のチェックを実行中...")


def check_file_size(folder_path):
    print("ファイルサイズのチェックを実行中...")


def main():
    # チェック対象のフォルダパスを指定
    folder_path = input("チェックするフォルダのパスを入力してください: ").strip()

    try:
        file_count = count_files_in_folder(folder_path)
        print(f"\n指定したフォルダには {file_count} 個のファイルがあります。")

        print("\n実行するチェックを選択してください:")
        print(" 1: ファイル形式のチェック")
        print(" 2: フォーマットの整合性のチェック")
        print(" 3: 命名規則のチェック")
        print(" 4: 音量レベルのチェック")
        print(" 5: 無音部分のチェック")
        print(" 6: ファイルサイズのチェック")
        print(" 7: すべてのチェックを実行")

        choice = input("\n番号を入力してください: ").strip()

        if choice == "1":
            check_file_format(folder_path)
        elif choice == "2":
            check_format_consistency(folder_path)
        elif choice == "3":
            check_naming_rules(folder_path)
        elif choice == "4":
            check_volume_level(folder_path)
        elif choice == "5":
            check_silence(folder_path)
        elif choice == "6":
            check_file_size(folder_path)
        elif choice == "7":
            print("\nすべてのチェックを実行中...")
            check_file_format(folder_path)
            check_format_consistency(folder_path)
            check_naming_rules(folder_path)
            check_volume_level(folder_path)
            check_silence(folder_path)
            check_file_size(folder_path)
        else:
            print("\n無効な選択です。スクリプトを終了します。")

    except ValueError as e:
        print(f"エラー: {e}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")


if __name__ == "__main__":
    main()
