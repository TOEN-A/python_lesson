import pygetwindow as gw
import pyautogui
import time
from datetime import datetime
from supabase import create_client, Client

# SupabaseのURLとAPIキーを設定
SUPABASE_URL = "https://betqlvuhgxgdynopdjxq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJldHFsdnVoZ3hnZHlub3BkanhxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTg1NTEyNDEsImV4cCI6MjAzNDEyNzI0MX0.sSVcWQMkFvU-SB35Iz22VuRAZw2rX9Fcf_qbw5TVB5w"

# Supabaseクライアントの作成
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def take_screenshot(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        if window:
            window.activate()
            time.sleep(1)  # アクティブ化後、少し待つ
            # 現在の日時を取得
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            # ファイル名に日時を追加
            filename = f"{window_title}_screenshot_{current_time}.png"
            screenshot = pyautogui.screenshot(
                region=(window.left, window.top, window.width, window.height)
            )
            screenshot.save(filename)
            print(f"スクリーンショットを {filename} として保存しました。")
            return filename
    except IndexError:
        print("指定されたタイトルのウィンドウが見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def upload_to_supabase(file_path):
    try:
        # Supabaseストレージにファイルをアップロード
        bucket_name = "pokemon-sa-screenshot"
        file_name_in_storage = file_path.split("/")[-1]  # ファイル名のみ取得
        response = supabase.storage.from_(bucket_name).upload(file_name_in_storage, file_path)

        if response.status_code == 200:
            print(f"{file_path} をSupabaseにアップロードしました。")
        else:
            print(f"アップロードに失敗しました: {response.text}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# VisualBoyAdvanceのウィンドウタイトルを指定してスクリーンショットを取る
file_path = take_screenshot("VisualBoyAdvance-M 2.1.9")
if file_path:
    upload_to_supabase(file_path)
