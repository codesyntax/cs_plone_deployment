from pathlib import Path


extra_lines = [
    "    debug_mode: true",
    "    verbose_security: true",

]

def main():
    if (Path("backend") / "instance.yaml").exists():
        with open(Path("backend") / "instance.yaml") as fp:
            lines = fp.readlines()
            lines.append("\n")
            for extra_line in extra_lines:
                if extra_line not in lines:
                    lines.append(f"{extra_line}\n")

        with open(Path("backend") / "instance.yaml", "w") as fp:
            fp.writelines(lines)

        print("Modified the instance.yaml file to add debug info")


if __name__ == '__main__':
    main()
