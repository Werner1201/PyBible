import sys
from controller.argcontroller import search_name, search_chapter, search_verse, load_bible


def main():
    args = sys.argv
    bible = load_bible()
    for arg in args:
        # Se for 1 == argumento de nome do livro
        if args.index(arg) == 1:
            print(search_name(arg, bible))
            pass
        # Se for 2 == argumento do num do capitulo
        if args.index(arg) == 2:
            search_chapter(arg, bible)
            pass
        # Se for 3 == argumento do num do versiculo
        if args.index(arg) == 3:
            search_verse(arg, bible)
            pass


if __name__ == "__main__":
    main()
    pass
