"""
Remove the devops folder in case it exists

"""
import os
from pathlib import Path
import shutil

def main():
    if (Path(os.getcwd()) / 'devops').exists():
        shutil.rmtree(Path(os.getcwd()) / "devops")
        print("Devops folder removed succesfully")


if __name__ == '__main__':
    main()
