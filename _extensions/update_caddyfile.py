"""
add password based basic authentication to /api URLs in Caddy
"""

from pathlib import Path
import bcrypt
import uuid


def _generate_password():
    password = uuid.uuid4().hex
    print(f"Password for /api URLs is: f{password}")
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def main():
    if (Path("frontend") / "Makefile").exists():
        new_contents = []
        with open(Path("deploy") / Path("conf") / "Caddyfile") as fp:
            for line in fp.readlines():
                new_line = line
                if line.find("XXXXXXXXXXX") != -1:
                    new_password = _generate_password().decode()
                    new_line = line.replace("XXXXXXXXXXX", new_password)
                new_contents.append(new_line)

        with open(Path("deploy") / Path("conf") / "Caddyfile", "w") as fp:
            fp.writelines(new_contents)


if __name__ == "__main__":
    main()
