import os
from pathlib import Path

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context):
        current_path = os.getcwd()
        current_folder_name = Path(current_path).name
        return {
            "project_name": current_folder_name,
            "image_prefix": f"registry.gitlab.com/{current_folder_name}",
            "is_volto": "frontend" in os.listdir("."),
            "is_classic": "frontend" not in os.listdir("."),
        }
