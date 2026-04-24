"""
Update the backend/src/profiles/default/metadata.xml to add install time dependencies
"""

from pathlib import Path
import argparse


def main(postgres=False, thumbor=False, python_code_path=""):
    if postgres:
        new_contents = []
        path_to_file = Path(python_code_path) / "profiles" / "default" / "metadata.xml"

        with open(path_to_file, "r") as fp:
            for line in fp.readlines():
                if line.strip() == "</dependencies>":
                    new_contents.append(
                        "    <dependency>profile-plone.pgcatalog:default</dependency>\n"
                    )
                    if thumbor:
                        new_contents.append(
                            "    <dependency>profile-plone.pgthumbor:default</dependency>\n"
                        )
                    new_contents.append(line)
                else:
                    new_contents.append(line)

        with open(path_to_file, "w") as fp:
            fp.writelines(new_contents)

        print("Updated profile metadata.xml")
    else:
        print("Nothing done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--postgres", type=str, required=True)
    parser.add_argument("--thumbor", type=str, required=True)
    parser.add_argument("--python_code_path", type=str, required=True)
    args = parser.parse_args()
    main(
        postgres=args.postgres == "True",
        thumbor=args.thumbor == "True",
        python_code_path=args.python_code_path,
    )
