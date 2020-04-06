from typing import List
from model.Livro import Livro


class Biblia:
    def __init__(self, biblia: List[Livro]):
        self.lista_de_livros = biblia
