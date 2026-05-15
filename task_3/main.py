import sys
from pathlib import Path
from colorama import init, Fore

if len(sys.argv) < 2:
    print(Fore.RED + "Будь ласка, вкажіть шлях до папки!")
    sys.exit()

path_string = sys.argv[1]
root_path = Path(path_string)

def show_directory(current_path, level=0):
    spaces = "  " * (level * 4)
    
    for item in current_path.iterdir():
           if item.is_dir():
                 print(spaces + Fore.BLUE + f" {item.name}")
                 show_directory(item, level + 1)
           else:
                print(spaces + Fore.YELLOW + f" {item.name}")

print(Fore.BLUE + f"Структура папки {root_path.name}:")
show_directory(root_path)