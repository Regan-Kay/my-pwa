import webbrowser
import winreg
import sys
import os

PWA_URL = "https://regan-kay.github.io/my-pwa/"
REG_NAME = "MyPWAStarter"

def add_to_startup():
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    # Full path to the exe
    exe_path = f'"{sys.executable}"'

    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            reg_path,
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, REG_NAME, 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
        print("Added to startup successfully")
    except Exception as e:
        print("Error adding to startup:", e)

def main():
    add_to_startup()
    webbrowser.open(PWA_URL)

if __name__ == "__main__":
    main()
