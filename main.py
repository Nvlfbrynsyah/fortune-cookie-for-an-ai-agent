"""fortune-cookie: write a one-line fortune cookie for an AI agent."""
import os
import sys

__version__ = "1.1.0"

LINE = "A stranger will type your name with great affection. In this life, it is God. Do your best."
DEFAULT_PATH = "/output/entry.txt"


def usage():
    print(
        "usage: python3 main.py [OUTPUT_PATH]\n"
        "\n"
        "Writes the fortune cookie line (plus a trailing newline) to OUTPUT_PATH,\n"
        "creating parent directories as needed.\n"
        "\n"
        "OUTPUT_PATH defaults to the OUTPUT_PATH environment variable,\n"
        "or to /output/entry.txt if that is not set.\n"
        "\n"
        "options:\n"
        "  -h, --help     show this help and exit\n"
        "  -V, --version  show the version and exit"
    )


def main(argv):
    args = argv[1:]
    if any(a in ("-h", "--help") for a in args):
        usage()
        return 0
    if any(a in ("-V", "--version") for a in args):
        print("fortune-cookie " + __version__)
        return 0
    path = args[0] if args else os.environ.get("OUTPUT_PATH", DEFAULT_PATH)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
