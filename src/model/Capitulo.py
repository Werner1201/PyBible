from model.Verso import Verso
from typing import List


class Capitulo:
    def __init__(self, index: int, versos: List[Verso]):
        self.index = index
        self.versos = versos

    def num_versos(self) -> int:
        return len(self.versos)

    def get_index(self) -> int:
        return self.index

    def get_versos(self) -> List[Verso]:
        return self.versos
