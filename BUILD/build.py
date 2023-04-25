from sys import platform
from os import system


if platform == "win32":
    system("rd /s /q build")
    system("rd /s /q dist")
    system("del /q *.spec")
    system(f'pyinstaller --noconfirm --onefile --icon "cli.ico" --add-data "../quora;." "../main.py"')
    system("del /q *.spec")
    system("rd /s /q build")
    system("rd /s /q %USERPROFILE%\AppData\Local\pyinstaller")
    system("explorer dist")

if platform == "linux" or platform == "linux2" or platform == "unix":
    print("Для данной системы не поддерживается автоматическая сборка (возможно в будущем добавлю)!")
    input()
