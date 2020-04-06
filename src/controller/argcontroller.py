from model.DbMapping import fill_bible
from model.Biblia import Biblia
from model.Capitulo import Capitulo
from model.Verso import Verso
from model.Livro import Livro
from fuzzywuzzy import fuzz
import click
from view.viewverses import showText


def init_bible() -> Biblia:
    return fill_bible()


def arg_range_parser(arg):
    list_ints = []
    linhas = str(arg).split('-')
    for string in linhas:
        if(linhas.index(string) > 0):
            list_ints.append(int(string))
        else:
            list_ints.append(int(string)-1)
    return list_ints


def check_len(index: list) -> bool:
    if len(index) > 1:
        return True
    else:
        False


def check_neg(num: int) -> bool:
    return True if num == -1 else False


def argParse(args: list, bible: Biblia) -> list:
    nome_livro = str(args[1])
    capitulo_nums = arg_range_parser(args[2])
    verso_nums = []
    try:
        verso_nums = arg_range_parser(args[3])
        pass
    except IndexError:
        verso_nums.append(-1)
        pass
    return [nome_livro, capitulo_nums, verso_nums, bible]


def tasks(parametros: list):
    livro = pesquisa(parametros[0], parametros[1],
                     parametros[2], parametros[3])
    return livro


def pesquisa(nome: str, capitulos_index: list, versos_index: list, bible: Biblia) -> Livro:
    livro_index = search_name(nome, bible)
    valid_cap = check_len(capitulos_index)
    valid_ver = check_neg(versos_index[0])
    capitulos = dados_dos_versos(livro_index, capitulos_index,
                                 versos_index, bible, valid_cap, valid_ver)
    return Livro(livro_index, nome, capitulos)


def search_name(book_arg, bible):
    nomes = index_books(bible)
    for nome in nomes:
        if fuzz.partial_token_sort_ratio(book_arg, nome) >= 80:
            return nomes.index(nome)


def dados_dos_versos(livro_index, capitulos_index, versos_index, bible, valid_cap, valid_ver) -> list:
    capitulos = []
    if(valid_ver and valid_cap):
        for capitulo in bible.lista_de_livros[livro_index].capitulos[capitulos_index[0]:capitulos_index[1]]:
            capitulos.append(capitulo)

        return capitulos


def index_books(bible):
    nomes = []
    for book in bible.lista_de_livros:
        nomes.append(book.nome.replace(" ", "").replace("ê", "e").replace("â", "a").replace("é", "e").replace(
            "ô", "o").replace("ó", "o").replace("í", "i").replace("ç", "c").replace("õ", "o").replace("ã", "a").replace("ú", "u").replace("á", "a"))
    return nomes
