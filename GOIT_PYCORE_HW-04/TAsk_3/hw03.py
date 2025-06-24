from pathlib import Path
import sys
from receive_path import parce_folder


if len(sys.argv) < 2:
    print("❗ Не вказано шлях до файлу. Передай шлях як аргумент.")
    sys.exit(1)
path = Path(sys.argv[1])

if __name__ == "__main__":
    parce_folder(Path(path),1)
