import webbrowser

def open_website(keyword):
    """
    指定されたキーワードに基づいてウェブサイトを開く関数
    """
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "miibo": "https://miibo.ai"
    }
    
    if keyword.lower() in websites:
        webbrowser.open(websites[keyword.lower()])
        return f"{keyword}のウェブサイトを開きました。"
    else:
        return f"{keyword}に対応するウェブサイトが見つかりません。"

def handle_user_input(user_input):
    """
    ユーザー入力を処理し、必要に応じてウェブサイトを開く関数
    """
    return open_website(user_input)

# メインのチャットループ
while True:
    user_input = input("キーワードを入力してください（終了するには'quit'と入力）: ")
    if user_input.lower() == 'quit':
        break
    
    response = handle_user_input(user_input)
    print(response)

print("プログラムを終了します。")
