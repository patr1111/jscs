import os
import email
from email import policy
from email.parser import BytesParser
import chardet

def extract_text_from_eml(eml_path):
    try:
        with open(eml_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        
        # 本文を取得
        text_content = []
        
        # 件名を取得（日本語対応）
        subject = msg.get('subject', '')
        if subject:
            text_content.append(f"件名: {subject}\n")
        
        # 本文を取得
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    payload = part.get_payload(decode=True)
                    # エンコーディングを検出
                    detected = chardet.detect(payload)
                    try:
                        decoded_text = payload.decode(detected['encoding'] or 'utf-8', errors='replace')
                        text_content.append(decoded_text)
                    except:
                        try:
                            decoded_text = payload.decode('iso-2022-jp', errors='replace')
                            text_content.append(decoded_text)
                        except:
                            text_content.append(payload.decode('utf-8', errors='replace'))
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                # エンコーディングを検出
                detected = chardet.detect(payload)
                try:
                    decoded_text = payload.decode(detected['encoding'] or 'utf-8', errors='replace')
                    text_content.append(decoded_text)
                except:
                    try:
                        decoded_text = payload.decode('iso-2022-jp', errors='replace')
                        text_content.append(decoded_text)
                    except:
                        text_content.append(payload.decode('utf-8', errors='replace'))
        
        return "\n".join(text_content)
    except Exception as e:
        return f"エラー: {eml_path} の処理中にエラーが発生しました: {str(e)}\n"

def main():
    # 入力フォルダのパス
    input_dir = r"C:\Users\ppppa\OneDrive\デスクトップ\アースアイズ"
    # 出力ファイルのパス
    output_file = os.path.join(input_dir, "combined_emails.txt")
    
    # 処理したファイル数をカウント
    processed_count = 0
    error_count = 0
    
    print("EMLファイルの処理を開始します...")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as out_f:
            # フォルダ内のすべてのEMLファイルを処理
            for filename in os.listdir(input_dir):
                if filename.lower().endswith('.eml'):
                    eml_path = os.path.join(input_dir, filename)
                    print(f"処理中: {filename}")
                    
                    # ファイル名を区切りとして書き込み
                    out_f.write(f"\n{'='*80}\n")
                    out_f.write(f"ファイル: {filename}\n")
                    out_f.write('='*80 + "\n\n")
                    
                    # EMLファイルの内容を抽出して書き込み
                    content = extract_text_from_eml(eml_path)
                    out_f.write(content)
                    out_f.write("\n\n")
                    
                    processed_count += 1
                    if "エラー:" in content:
                        error_count += 1
    
        print(f"\n処理が完了しました。")
        print(f"処理したファイル数: {processed_count}")
        print(f"エラーが発生したファイル数: {error_count}")
        print(f"結果は以下のファイルに保存されました: {output_file}")
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main() 