import json
import os
from fuzzywuzzy import fuzz


def index_books(bible):
    nomes = []
    for book in bible:
        nomes.append(book["name"].replace(" ", "").replace("ê", "e").replace("â", "a").replace("é", "e").replace(
            "ô", "o").replace("ó", "o").replace("í", "i").replace("ç", "c").replace("õ", "o").replace("ã", "a").replace("ú", "u").replace("á", "a"))
    return nomes



def search_name(book_arg, bible):
    nomes = index_books(bible)
    for nome in nomes:
        if fuzz.partial_token_sort_ratio(book_arg, nome) >= 80:
            return nomes.index(nome)


def search_chapter(chapter_arg, bible):
    print(chapter_arg)
    pass


def search_verse(verse_arg, bible):
    print(verse_arg)
    pass


def load_bible():
    with open(os.path.abspath('./model/aa.json'), 'r', encoding='utf-8') as json_file:
        bible = json.load(json_file)
    return bible
