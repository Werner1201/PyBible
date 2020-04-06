class Verso():
    def __init__(self, index: int, conteudo: str):
        self.index = index
        self.conteudo = conteudo

    def get_index(self) -> int:
        return self.index

    def get_conteudo(self) -> str:
        return self.conteudo
