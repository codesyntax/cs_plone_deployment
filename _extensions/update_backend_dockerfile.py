"""
Update the Makefile in the backend folder, to update the docker image name wherever it is shown

"""

import os
from pathlib import Path


def main():
    new_contents = []
    COPY_ZOPE_INI = False
    MOUNT_TYPE_SSH = False
    APT_UPDATE = False
    SSH_CONFIG = False

    with open(Path("backend") / "Dockerfile") as fp:
        lines = fp.readlines()
        # Copy custom zope.ini to the built image
        # this will disable the access log
        if "COPY zope.ini etc/" not in lines:
            COPY_ZOPE_INI = True
        if "RUN --mount=type=ssh,id=default <<EOT" not in lines:
            MOUNT_TYPE_SSH = True
        if "RUN apt-get update && apt-get install -y openssh-client git" not in lines:
            APT_UPDATE = True
        if (
            'RUN mkdir -p ~/.ssh && echo "Host *\\n\\tStrictHostKeyChecking no\\n\\n" > ~/.ssh/config'
            not in lines
        ):
            SSH_CONFIG = True

        for line in lines:
            if COPY_ZOPE_INI and line.startswith("COPY . src"):
                new_contents.append(line)
                new_contents.append("COPY zope.ini etc/\n")
            elif MOUNT_TYPE_SSH and line.startswith("RUN <<EOT"):
                new_contents.append("RUN --mount=type=ssh,id=default <<EOT\n")
            elif line.startswith("WORKDIR /app"):
                if APT_UPDATE:
                    new_contents.append(
                        "RUN apt-get update && apt-get install -y openssh-client git\n"
                    )
                if SSH_CONFIG:
                    new_contents.append(
                        'RUN mkdir -p ~/.ssh && echo "Host *\\n\\tStrictHostKeyChecking no\\n\\n" > ~/.ssh/config\n'
                    )
                new_contents.append(line)

            else:
                new_contents.append(line)

    with open(Path("backend") / "Dockerfile", "w") as fp:
        fp.writelines(new_contents)

    print("Updated backend Dockerfile")


if __name__ == "__main__":
    main()
