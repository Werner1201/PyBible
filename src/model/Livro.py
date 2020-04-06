from typing import List
from model.Capitulo import Capitulo


class Livro:
    def __init__(self, index: int, nome: str, capitulos: List[Capitulo]):
        self.index = index
        self.nome = nome
        self.capitulos = capitulos

    def num_capitulos(self) -> int:
        return len(self.capitulos)

    def get_index(self) -> int:
        return self.index

    def get_nome(self) -> str:
        return self.nome
