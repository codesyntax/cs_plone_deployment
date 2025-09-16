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

            elif line.startswith("\t@docker build . -t"):
                # we do several things here:
                # 1. add the --ssh default
                new_line = line.replace(
                    "@docker build . -t",
                    "@docker build --ssh default . -t",
                )
                # 2. change the separator for the docker image name
                new_line = new_line.replace(
                    "$(IMAGE_NAME_PREFIX)-backend-acceptance:",
                    "$(IMAGE_NAME_PREFIX)/backend-acceptance:",
                )
                new_line = new_line.replace(
                    "$(IMAGE_NAME_PREFIX)-backend:", "$(IMAGE_NAME_PREFIX)/backend:"
                )
                new_contents.append(new_line)
            else:
                new_contents.append(line)

    with open(Path("backend") / "Makefile", "w") as fp:
        fp.writelines(new_contents)

    print("Updated backend Makefile")


if __name__ == "__main__":
    main()
