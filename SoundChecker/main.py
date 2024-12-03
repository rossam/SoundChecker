import os
import wave
import re


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
                        # チャネル情報を取得（有効性の確認）
                        wav_file.getnchannels()
                except wave.Error:
                    print(f"エラー: {file} はWAV形式ではありません。")
                except Exception as e:
                    print(f"エラー: {file} のチェック中に予期しないエラーが発生しました: {e}")


def check_format_consistency(folder_path, sample_rate=44100, sample_width=2, channels=2):
    """
    フォーマットの整合性をチェックする
    :param sample_rate: 指定のサンプルレート（例: 44100Hz）
    :param sample_width: 指定のビット深度（例: 16bit = 2bytes）
    :param channels: 指定のチャンネル数（例: ステレオ=2）
    """
    print("フォーマットの整合性をチェック中...")
    for root, _, files in os.walk(folder_path):
        for file in files:
            if not file.lower().endswith(".wav"):
                continue  # WAV以外はスキップ

            file_path = os.path.join(root, file)
            try:
                with wave.open(file_path, 'rb') as wav_file:
                    actual_sample_rate = wav_file.getframerate()
                    actual_sample_width = wav_file.getsampwidth()
                    actual_channels = wav_file.getnchannels()

                    # サンプルレートのチェック
                    if actual_sample_rate != sample_rate:
                        print(f"エラー: {file} のサンプルレートが不一致です（{actual_sample_rate} != {sample_rate}）")
                    # ビット深度のチェック
                    elif actual_sample_width != sample_width:
                        print(f"エラー: {file} のビット深度が不一致です（{actual_sample_width} != {sample_width}）")
                    # チャンネル数のチェック
                    elif actual_channels != channels:
                        print(f"エラー: {file} のチャンネル数が不一致です（{actual_channels} != {channels}）")

            except Exception as e:
                print(f"エラー: {file} のチェック中に予期しないエラーが発生しました: {e}")


def check_naming_rules(folder_path, naming_pattern=r"^file\d+_[A-Za-z0-9_]+\.wav$"):
    """
    命名規則の遵守をチェックする
    :param folder_path: チェック対象のフォルダパス
    :param naming_pattern: 命名規則の正規表現（デフォルトは "file+数字_任意の文字列.wav"）
    """
    print("\n命名規則のチェックを開始します...")

    # 正規表現パターンをコンパイル
    pattern = re.compile(naming_pattern)

    for root, _, files in os.walk(folder_path):
        for file in files:
            # .wavファイルのみチェック
            if not file.lower().endswith(".wav"):
                continue

            file_path = os.path.join(root, file)

            # ファイル名が命名規則に従っているかチェック
            if not pattern.match(file):
                print(f"エラー: {file} は命名規則に違反しています。")


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
