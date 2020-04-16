import sys
from controller.argcontroller import init_bible, argParse, tasks
from view.viewverses import showText


def main() -> None:
    args = sys.argv
    biblia = init_bible()
    showText(tasks(argParse(args, biblia)))


if __name__ == "__main__":
    main()
    pass
