from model.DbMapping import fill_bible
from model.Biblia import Biblia
from model.Capitulo import Capitulo
from model.Verso import Verso
from model.Livro import Livro
from fuzzywuzzy import fuzz


def init_bible() -> Biblia:
    """
    Essa Funcao puxa a funcao onde carrega uma unica vez os dados da Biblia.
    Para ser chamada na camada main passando pela camada de controle.
    """
    return fill_bible()


def arg_range_parser(arg: str) -> list:
    """
    Essa Funcao eh um parser que separa 2 strings transforma-as em ints e as coloca em uma lista.
    A verificacao serve para transformar o index em um legivel pelas listas.
    """
    list_ints = []
    linhas = str(arg).split('-')
    for string in linhas:
        if(linhas.index(string) > 0):
            list_ints.append(int(string))
        else:
            list_ints.append(int(string)-1)
    return list_ints


def check_len(index: list) -> bool:
    """
    Essa Funcao serve para verificar se o tamanho da lista eh maior que 1
    """
    if len(index) > 1:
        return True
    else:
        False


def check_neg(num: int) -> bool:
    """
    Essa Funcao serve para verificar se o primeiro registro da lista contem '-1'
    """
    return True if num == -1 else False


def argParse(args: list, bible: Biblia) -> list:
    """
    Essa Funcao eh um parser geral onde ele separa e tipifica:
    O Nome do livro, O Range de Capitulos e tenta associar o Range de Versos.
    E retorna uma lista com esses valores + O objeto da Biblia Real.
    """
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


def tasks(parametros: list) -> Livro:
    """
    Essa Funcao eh um middleware para passar os argumentos parseados para a Funcao 
    Pesquisa que retorna o Livro pra retornarmos a View
    """
    livro = pesquisa(parametros[0], parametros[1],
                     parametros[2], parametros[3])
    return livro


def pesquisa(nome: str, capitulos_index: list, versos_index: list, bible: Biblia) -> Livro:
    """
    Essa Funcao Realiza toda a indexacao das subfuncoes de pesquisas e verificacoes.
    Onde o Index do Livro, as validacoes dos numeros de capitulos e versos sao feitos.
    Passados esses para a funcao dados_dos_versos que retorna os capitulos pedidos onde 
    Cria-se um objeto Livro para o retorno do Mesmo.
    """
    livro_index = search_name(nome, bible)
    valid_cap = check_len(capitulos_index)
    valid_ver = check_neg(versos_index[0])
    capitulos = dados_dos_versos(livro_index, capitulos_index,
                                 versos_index, bible, valid_cap, valid_ver)
    return Livro(livro_index, bible.lista_de_livros[livro_index].get_nome(), capitulos)


def search_name(book_arg: str, bible: Biblia) -> int:
    """
    Essa funcao verifica um livro proximo a string pedida e retorna o index do livro pedido.
    """
    nomes = index_books(bible)
    for nome in nomes:
        if fuzz.partial_token_sort_ratio(book_arg, nome) >= 80:
            return nomes.index(nome)


def dados_dos_versos(livro_index: int, capitulos_index: list, versos_index: list, bible: Biblia, valid_cap: bool, valid_ver: bool) -> list:
    """
    Nessa Funcao existem 3 controles para cada tipo de situaca/pedido.
    Mas existe apenas 1 retorno a lista de capitulos mesmo que a lista contenha apenas 1 elemento.
    Situacao 1: Se valid_ver for -1 e valid_cap tiver multiplos indexes mostra todos capitulos pedidos
    Situacao 2: Se valid_ver nao for -1 e ainda assim valid_cap tiver multiplos indexes usamos apenas um index
    e retiramos apenas os versiculos pedidos
    Situacao 3: Se valid_ver nao for -1 e houver apenas 1 capitulo
    """
    capitulos_cru = []
    versos_cru = []
    # Se valid_ver for -1 e valid_cap tiver multiplos indexes mostra todos capitulos pedidos
    if(valid_ver and valid_cap):
        for capitulo in bible.lista_de_livros[livro_index].capitulos[capitulos_index[0]:capitulos_index[1]]:
            capitulos_cru.append(capitulo)

    # Se valid_ver nao for -1 e ainda assim valid_cap tiver multiplos indexes usamos apenas um index
    # e retiramos apenas os versiculos pedidos
    if(not valid_ver and valid_cap):
        capitulo = bible.lista_de_livros[livro_index].capitulos[capitulos_index[0]]
        try:
            for verso in capitulo.versos[versos_index[0]: versos_index[1]]:
                versos_cru.append(verso)
        except IndexError:
            verso = capitulo.versos[versos_index[0]]
            versos_cru.append(verso)
        finally:
            capitulo.versos = versos_cru
            capitulos_cru.append(capitulo)

    # Se valid_ver nao for -1 e houver apenas 1 capitulo
    if(not valid_ver and not valid_cap):
        capitulo = bible.lista_de_livros[livro_index].capitulos[capitulos_index[0]]
        try:
            for verso in capitulo.versos[versos_index[0]: versos_index[1]]:
                versos_cru.append(verso)
        except IndexError:
            verso = capitulo.versos[versos_index[0]]
            versos_cru.append(verso)
        finally:
            capitulo.versos = versos_cru
            capitulos_cru.append(capitulo)

    return capitulos_cru


def index_books(bible: Biblia) -> list:
    """
    Essa funcao eh responsavel por facilitar a funcao de pesquisa do nome do livro pedido.
    Trocando os carateres do Brasil por caracteres normais.
    """
    nomes = []
    for book in bible.lista_de_livros:
        nomes.append(book.nome.replace(" ", "").replace("ê", "e").replace("â", "a").replace("é", "e").replace(
            "ô", "o").replace("ó", "o").replace("í", "i").replace("ç", "c").replace("õ", "o").replace("ã", "a").replace("ú", "u").replace("á", "a").replace("Ê", "E"))
    return nomes
