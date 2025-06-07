import os
import sys
import requests
import zipfile
import shutil
from pathlib import Path

def get_poppler_dir():
    # ユーザーのホームディレクトリにインストール
    home = os.path.expanduser("~")
    return os.path.join(home, "poppler-23.11.0")

def download_poppler():
    print("Popplerのダウンロードとインストールを開始します...")
    
    # ダウンロードURL
    poppler_url = "https://github.com/oschwartz10612/poppler-windows/releases/download/v23.11.0-0/Release-23.11.0-0.zip"
    install_dir = get_poppler_dir()
    zip_path = "poppler.zip"
    temp_dir = "poppler_temp"
    
    try:
        # 既存のインストールをチェック
        if os.path.exists(install_dir):
            print(f"Popplerは既にインストールされています: {install_dir}")
            print("インストールディレクトリの内容:")
            for root, dirs, files in os.walk(install_dir):
                level = root.replace(install_dir, '').count(os.sep)
                indent = ' ' * 4 * level
                print(f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print(f"{subindent}{f}")
            return True
        
        # 一時ファイルの削除（もし存在する場合）
        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        
        # ZIPファイルをダウンロード
        print("Popplerをダウンロード中...")
        response = requests.get(poppler_url, stream=True)
        response.raise_for_status()
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # ZIPファイルを解凍
        print("ファイルを展開中...")
        os.makedirs(temp_dir, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # ZIPファイルの内容を表示
            print("ZIPファイルの内容:")
            for name in zip_ref.namelist():
                print(f"  {name}")
            zip_ref.extractall(temp_dir)
        
        # 展開されたファイルの構造を確認
        print("\n展開されたファイルの構造:")
        for root, dirs, files in os.walk(temp_dir):
            level = root.replace(temp_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
        
        # インストールディレクトリを作成
        os.makedirs(install_dir, exist_ok=True)
        
        # ファイルを移動（直接tempフォルダの内容を移動）
        print("\nファイルを移動中...")
        for item in os.listdir(temp_dir):
            s = os.path.join(temp_dir, item)
            d = os.path.join(install_dir, item)
            print(f"移動: {s} -> {d}")
            if os.path.isdir(s):
                if os.path.exists(d):
                    shutil.rmtree(d)
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        
        # インストール後のファイル構造を確認
        print("\nインストール後のファイル構造:")
        for root, dirs, files in os.walk(install_dir):
            level = root.replace(install_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f"{subindent}{f}")
        
        # 一時ファイルを削除
        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        
        print("Popplerのインストールが完了しました")
        return True
        
    except Exception as e:
        # エラー時の一時ファイルのクリーンアップ
        if os.path.exists(zip_path):
            os.remove(zip_path)
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        print(f"Popplerのインストール中にエラーが発生しました: {str(e)}")
        return False

if __name__ == "__main__":
    download_poppler() 