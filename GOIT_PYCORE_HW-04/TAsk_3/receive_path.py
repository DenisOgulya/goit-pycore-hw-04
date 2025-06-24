from pathlib import Path
from colorama import Fore


def parce_folder(path,level):
    for el in path.iterdir():
        if el.is_dir(): # перевірка ти директорія є папакою
            print(f"{"  " * level}{Fore.BLUE}{el.name}/")
            lvl=level+1
            parce_folder(el, lvl)  
        else:
            print(f"{"  " * level}{Fore.GREEN}{el.name}")
    
    

