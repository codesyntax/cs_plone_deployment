"""
Update the Makefile in the backend folder, to update the docker image name wherever it is shown

"""

import os
from pathlib import Path


def main():
    new_contents = []
    with open(Path("backend") / "Dockerfile") as fp:
        lines = fp.readlines()
        if "COPY zope.ini etc/" not in lines:
            for line in lines:
                if line.startswith("COPY . src"):
                    new_contents.append(line)
                    new_contents.append("COPY zope.ini etc/")
                else:
                    new_contents.append(line)

    with open(Path("backend") / "Dockerfile", "w") as fp:
        fp.writelines(new_contents)

    print("Updated backend Dockerfile")


if __name__ == "__main__":
    main()
