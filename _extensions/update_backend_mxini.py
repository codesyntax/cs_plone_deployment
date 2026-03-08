"""
Update the mx.ini file in backend to add thumbor development dependency
"""

import argparse
from pathlib import Path


def main(thumbor=False):
    if thumbor:
        with open(Path("backend") / "mx.ini", "a") as fp:
            fp.write("[plone-pgthumbor]\n")
            fp.write("url = https://github.com/erral/plone-pgthumbor\n")
            fp.write("branch = plone-6.1-support\n")

        print("Updated backend mx.ini")
    else:
        print("Nothing done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--thumbor", type=str, required=True)
    args = parser.parse_args()
    main(thumbor=args.thumbor == "True")
