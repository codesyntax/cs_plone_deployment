"""Set the initial version of the project to 1.0.0.

This script updates all files tracked by release-it/bumper:
- version.txt
- deploy/.env (VERSION property)
- backend Python version file
- frontend/package.json (Volto projects only)
- frontend addon package.json (Volto projects only)
"""

import json
import os
import re
import tomllib
from pathlib import Path


VERSION = "1.0.0"


def update_version_txt():
    """Update version.txt with the initial version."""
    version_file = Path("version.txt")
    version_file.write_text(f"{VERSION}\n")
    print(f"  Updated: version.txt")


def update_deploy_env():
    """Update VERSION in deploy/.env."""
    env_file = Path("deploy/.env")
    if env_file.exists():
        content = env_file.read_text()
        content = re.sub(r"^VERSION=.*$", f"VERSION={VERSION}", content, flags=re.MULTILINE)
        env_file.write_text(content)
        print(f"  Updated: deploy/.env")


def update_python_version_file():
    """Update the backend Python version file."""
    pyproject = Path("backend/pyproject.toml")
    if not pyproject.exists():
        print("  Warning: backend/pyproject.toml not found")
        return

    with open(pyproject, "rb") as fp:
        toml = tomllib.load(fp)
        python_version_file = toml["tool"]["hatch"]["version"]["path"]

    version_file = Path("backend") / python_version_file
    if version_file.exists():
        content = version_file.read_text()
        content = re.sub(r'^__version__ = .*$', f'__version__ = "{VERSION}"', content, flags=re.MULTILINE)
        version_file.write_text(content)
        print(f"  Updated: backend/{python_version_file}")
    else:
        print(f"  Warning: backend/{python_version_file} not found")


def update_package_json(package_path: Path):
    """Update version in a package.json file."""
    if package_path.exists():
        with open(package_path, "r") as fp:
            data = json.load(fp)
        data["version"] = VERSION
        with open(package_path, "w") as fp:
            json.dump(data, fp, indent=2)
            fp.write("\n")
        print(f"  Updated: {package_path}")
    else:
        print(f"  Warning: {package_path} not found")


def update_frontend_packages():
    """Update frontend package.json files (Volto projects only)."""
    frontend_path = Path("frontend")
    if not frontend_path.exists():
        return

    # Update main frontend/package.json
    update_package_json(frontend_path / "package.json")

    # Update addon package.json
    packages_path = frontend_path / "packages"
    if packages_path.exists():
        addons = list(packages_path.iterdir())
        if addons:
            addon_name = addons[0].name
            update_package_json(packages_path / addon_name / "package.json")


def main():
    print(f"Setting project version to {VERSION}...")
    update_version_txt()
    update_deploy_env()
    update_python_version_file()
    update_frontend_packages()
    print(f"\nVersion set to {VERSION} successfully!")


if __name__ == "__main__":
    main()
