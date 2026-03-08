from pathlib import Path
import yaml
import argparse
import os

extra_lines = [
    "    debug_mode: true",
    "    verbose_security: true",
]


def main(postgres=False, thumbor=False, security_key=""):

    instance_path = Path("backend") / "instance.yaml"
    if instance_path.exists():
        # 1. Read the YAML into a Python dictionary
        with open(instance_path, "r") as fp:
            data = yaml.safe_load(fp) or {}

        # 2. Add or update the keys directly
        default_context = data.get("default_context", {})

        default_context["wsgi_listen"] = "0.0.0.0:8080"
        default_context["debug_mode"] = True
        default_context["verbose_security"] = True

        if postgres:
            default_context["db_storage"] = "pgjsonb"
            default_context["db_pgjsonb_dsn"] = (
                "dbname='zodb' user='zodb' password='zodb' host='localhost' port='5433'"
            )
            default_context["db_pgjsonb_history_preserving"] = True

        if thumbor:
            environment = default_context.get("environment", {})
            environment["PGTHUMBOR_SECURITY_KEY"] = security_key
            environment["PGTHUMBOR_SERVER_URL"] = "http://thumbor.127.0.0.1.nip.io:8888"
            default_context["environment"] = environment

        data["default_context"] = default_context

        # 3. Write it back safely
        with open(instance_path, "w") as fp:
            yaml.safe_dump(data, fp, default_flow_style=False)

        print("Modified the instance.yaml file to add debug info")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--postgres", type=str, required=True)
    parser.add_argument("--thumbor", type=str, required=True)
    parser.add_argument("--security_key", type=str, required=True)
    args = parser.parse_args()

    main(
        postgres=args.postgres == "True",
        thumbor=args.thumbor == "True",
        security_key=args.security_key,
    )
