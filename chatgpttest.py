import openai
import os

# OpenAI APIキーを設定
openai.api_key = 'YOUR_API_KEY'

def send_to_chatgpt(text=None, image_path=None, comment1=None, comment2=None):
    chat_history = [{"role": "system", "content": "You are a helpful assistant."}]
    
    if text:
        # 引数textが指定されている場合、文章のみ送信
        chat_history.append({"role": "user", "content": text})
    else:
        # 画像情報とコメントを組み合わせて送信
        if image_path and os.path.exists(image_path):
            image_message = f"Sending image: {image_path}"
            if comment1:
                image_message += f"\n{comment1}"
            if comment2:
                image_message += f"\n{comment2}"
            chat_history.append({"role": "user", "content": image_message})
        else:
            return "画像が見つかりません。"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # モデル名を指定
            messages=chat_history
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"エラーが発生しました: {e}"

# テストのための呼び出し
# 文章のみ送信
print(send_to_chatgpt(text="Hello! How can I assist you today?"))

# 画像とコメントを送信
print(send_to_chatgpt(image_path="path/to/your/image.png", comment1="This is the first comment.", comment2="This is the second comment."))
