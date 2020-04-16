from __future__ import print_function
from clint.textui import puts, colored, indent


def showText(livro):
    nome = livro.nome
    inicio = livro.capitulos[0].versos[0].get_index()
    index = inicio + 1
    capIndex = 0
    with indent(2, quote=' '):
        puts("{}".format(nome))
        for capitulo in livro.capitulos:
            if capIndex != capitulo.get_index():
                index = 1
            capIndex = capitulo.get_index()
            for verso in capitulo.versos:
                with indent(4, quote=' '):
                    puts("{}:{}".format(capitulo.get_index() +
                                        1, index) + " " + verso.get_conteudo())
                    index += 1

    print()
