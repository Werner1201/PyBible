import json
import os
from fuzzywuzzy import fuzz
import click
from view.viewverses import showText
import model


def check_range_chap(arg):
    if "-" in arg:
        strverses = arg.split('-')
        chapters = [int(strverses[0]) - 1, int(strverses[1])]
        return chapters


def check_only_chap(arg):
    if arg.isdigit:
        chapter = int(arg)-1
        return chapter


def check_only_verse(arg):
    if arg.isnumeric:
        verse = int(arg)-1
        return verse


def check_range_verse(arg):
    if "-" in arg:
        strverses = arg.split('-')
        verses = [int(strverses[0])-1, int(strverses[1])]
        return verses


def assignTask(args, bible):
    index_book = search_name(args[1], bible)
    chapters = check_range_chap(args[2])
    book_chapter = []
    book_chapters = []
    book_verse = []
    book_verses = []
    if(chapters == None):
        chapter = check_only_chap(args[2])
        book_chapter = search_chapter(index_book, chapter, bible)
    else:
        book_chapters = search_chapters(index_book, chapters, bible)

    verses = check_range_verse(args[3])
    if(verses == None):
        verse = check_only_verse(args[3])
        book_verse = search_verse(verse, book_chapter)
    else:
        book_verses = search_verses(verses, book_chapter)

    return [index_book, bible[index_book]["name"],
            chapter, verses, book_verses]


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


def search_chapters(book, chapter_arg, bible):
    name = bible[book]["name"]
    book_chapters = bible[book]["chapters"][chapter_arg[0]:chapter_arg[1]]
    return [book_chapters, chapter_arg]


def search_verses(verse_arg, bible):
    book_verses = bible[int(verse_arg[0]): int(verse_arg[1])]
    return book_verses


def search_chapter(book, chapter_arg, bible):
    book_chapter = bible[book]["chapters"][chapter_arg]
    return book_chapter


def search_verse(verse, bible):
    book_verse = bible[verse]
    return book_verse


def load_bible():
    os.chdir(os.path.dirname(__file__))
    with open(os.path.abspath("../model/aa.json"), 'r', encoding='utf-8') as json_file:
        bible = json.load(json_file)
    return bible
