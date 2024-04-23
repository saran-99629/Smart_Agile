import pyautogui
import time
import subprocess

def is_browser_window_open():
    
    process = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return b'chrome.exe' in output  

def capture_screenshots_with_browser(interval=10, duration=60):
    end_time = time.time() + duration
    i=1
    while time.time() < end_time:
        if is_browser_window_open():
            screenshot = pyautogui.screenshot()
            screenshot.save(f'{i}.png')
        time.sleep(interval)
        i+=1

capture_screenshots_with_browser(interval=10, duration=60)
