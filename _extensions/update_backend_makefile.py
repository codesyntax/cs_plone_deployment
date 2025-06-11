"""
Update the Makefile in the backend folder, to update the docker image name wherever it is shown

"""

import os
from pathlib import Path


def main():
    new_contents = []
    with open(Path("backend") / "Makefile") as fp:
        for line in fp.readlines():
            if line.startswith("IMAGE_NAME_PREFIX="):
                current_path = os.getcwd()
                current_folder_name = Path(current_path).name
                new_line = f"IMAGE_NAME_PREFIX=registry.gitlab.com/codesyntax/{current_folder_name}\n"
                new_contents.append(new_line)
            elif line.find("$(IMAGE_NAME_PREFIX)-backend:") != -1:
                new_line = line.replace("$(IMAGE_NAME_PREFIX)-backend:", "$(IMAGE_NAME_PREFIX)/backend:")
                new_contents.append(new_line)
            elif line.find("$(IMAGE_NAME_PREFIX)-backend-acceptance:") != -1:
                new_line = line.replace("$(IMAGE_NAME_PREFIX)-backend-acceptance:", "$(IMAGE_NAME_PREFIX)/backend-acceptance:")
                new_contents.append(new_line)
            else:
                new_contents.append(line)

    with open(Path("backend") / "Makefile", 'w') as fp:
        fp.writelines(new_contents)

    print("Updated backend Makefile")


if __name__ == '__main__':
    main()
