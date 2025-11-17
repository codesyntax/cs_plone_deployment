"""
Update the pyproject.toml file in backend to add `Plone` as dependency
"""

import tomllib
import tomli_w
from pathlib import Path


# cookieplone adds Products.CMFPlone as a dependency
# we want to get the exact version that it adds
# and replace it with Plone
PLONE_VERSION_DEPENDENCY = "Products.CMFPlone"

# All this dependencies are already provided by Plone package
# so there is no need to add them manually
DEPENDENCIES_TO_REMOVE = [
    "plone.api",
    "plone.app.caching",
    "plone.app.discussion",
    "plone.app.iterate",
    "plone.app.multilingual",
    "plone.app.upgrade",
    "plone.classicui",
    "plone.distribution",
    "plone.exportimport",
    "plone.restapi",
    "plone.volto",
    "Products.CMFPlacefulWorkflow",
]


def handle_dependency(dependency: str) -> str:
    """check the value of the dependency and act according to its presence
    in one of the lists above
    """
    if dependency.startswith(PLONE_VERSION_DEPENDENCY):
        name, version = dependency.split("==")
        return f"Plone=={version}"

    if dependency in DEPENDENCIES_TO_REMOVE:
        return ""

    return dependency


def main():
    new_dependencies = []
    toml_file = {}
    with open(Path("backend") / "pyproject.toml", "rb") as fp:
        toml_file = tomllib.load(fp)
        new_dependencies = []
        for dependency in toml_file["project"]["dependencies"]:
            new_dependency = handle_dependency(dependency)
            if new_dependency:
                new_dependencies.append(new_dependency)

    toml_file["project"]["dependencies"] = new_dependencies

    with open(Path("backend") / "pyproject.toml", "wb") as fp:
        tomli_w.dump(toml_file, fp)

    print("Updated backend pyproject.toml")


if __name__ == "__main__":
    main()
