from questionary import select
import os
import sys
from pyfiglet import Figlet


class Main:
    def __init__(self):
        # Инициализация не требует параметра loader
        pass

    def menu(self):
        print(Figlet().renderText("PY GRUB"))  # Исправлено создание объекта Figlet

        choice = select(  # Переименовано в choice вместо loader
            "PY GRUB ver 1.0",
            qmark='#',
            choices=["Boot in jinstall", "Reboot"]
        ).ask()

        if choice == "Boot in jinstall":  # Правильное сравнение значения выбора
            os.system('cls' if os.name == 'nt' else 'clear')
            # Универсальный запуск Python скрипта
            python = 'python3' if os.name != 'nt' else 'python'
            os.system(f'{python} install.py')

        elif choice == "Reboot":
            print("System rebooting...")
            sys.exit(0)  # Или os.system('reboot') для реальной перезагрузки


if __name__ == '__main__':
    Main().menu()