import pygetwindow as gw
import pyautogui
import time
from datetime import datetime


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
    except IndexError:
        print("指定されたタイトルのウィンドウが見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")


# VisualBoyAdvanceのウィンドウタイトルを指定してスクリーンショットを取る
take_screenshot("VisualBoyAdvance-M 2.1.9")
