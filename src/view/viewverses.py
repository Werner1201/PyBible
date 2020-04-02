from __future__ import print_function
from clint.textui import puts, colored, indent


def showText(book, capitulo, verso, text):
    inicio = verso[0]
    index = inicio + 1
    with indent(0, quote=' '):
        puts(colored.green("{}".format(book)))
        for linha in text:
            with indent(4, quote=' '):
                puts(colored.blue("{}:{}".format(
                    capitulo + 1, index)) + " " + str(linha))
                index += 1
    print()
