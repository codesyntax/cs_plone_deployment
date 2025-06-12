import os
import tomllib
from pathlib import Path
try:
    from copier_templates_extensions import ContextHook
except:
    ContextHook = object


class ContextUpdater(ContextHook):
    def hook(self, context):
        current_path = os.getcwd()
        current_folder_name = Path(current_path).name

        # Frontend Add-on name
        frontend_addon_name = "volto-dummy"
        frontend_packages = os.listdir(Path(current_path) / "frontend" / "packages")
        if frontend_packages:
            frontend_addon_name = frontend_packages[0]

        # Backend addon path
        python_version_file = ""
        pyproject = Path(current_path) / "backend" / "pyproject.toml"
        with open(pyproject, "rb") as fp:
            toml = tomllib.load(fp)
            python_version_file = toml['tool']['hatch']['version']['path']

        return {
            "project_name": current_folder_name,
            "image_prefix": f"registry.gitlab.com/{current_folder_name}",
            "is_volto": "frontend" in os.listdir("."),
            "is_classic": "frontend" not in os.listdir("."),
            "frontend_addon_name": frontend_addon_name,
            "python_version_file": python_version_file
        }
