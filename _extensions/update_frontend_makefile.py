"""
Update the Makefile in the backend folder, to update the docker image name wherever it is shown

"""

import os
from pathlib import Path


def main():
    new_contents = []
    if Path("frontend") / "Makefile":
        with open(Path("frontend") / "Makefile") as fp:
            for line in fp.readlines():
                if line.startswith("IMAGE_NAME="):
                    current_path = os.getcwd()
                    current_folder_name = Path(current_path).name
                    new_line = f"IMAGE_NAME=registry.gitlab.com/codesyntax/{current_folder_name}/frontend\n"
                    new_contents.append(new_line)
                else:
                    new_contents.append(line)

        with open(Path("frontend") / "Makefile", "w") as fp:
            fp.writelines(new_contents)

        print("Updated frontend Makefile")
    else:
        print("There is no frontend, nothing was done")


if __name__ == "__main__":
    main()
