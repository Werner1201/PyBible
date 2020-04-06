from model.Biblia import Biblia
from model.Livro import Livro
from model.Capitulo import Capitulo
from model.Verso import Verso
import json
import os


def fill_bible() -> Biblia:
    biblia = popula_biblia(load_bible())

    return biblia


def load_bible():
    os.chdir(os.path.dirname(__file__))
    with open(os.path.abspath("aa.json"), 'r', encoding='utf-8') as json_file:
        bible = json.load(json_file)
    return bible


def popula_biblia(biblia_crua: list) -> Biblia:
    biblia = 0
    livros = []
    for livro in biblia_crua:
        index = biblia_crua.index(livro)
        nome = livro["name"]
        capitulos = livro["chapters"]
        livros.append(popula_livros(index, nome, capitulos))
    biblia = Biblia(livros)

    return biblia


def popula_livros(index: int, nome: str, capitulos: list) -> Livro:
    lista_capitulos = []
    for capitulo in capitulos:
        lista_capitulos.append(popula_capitulos(
            capitulos.index(capitulo), capitulo))
    return Livro(index, nome, lista_capitulos)


def popula_capitulos(index: int, versos: list) -> Capitulo:
    lista_versos = []
    for verso in versos:
        lista_versos.append(popula_versos(versos.index(verso), verso))
    return Capitulo(index, lista_versos)


def popula_versos(index: int, conteudo: str) -> Verso:
    return Verso(index, conteudo)
