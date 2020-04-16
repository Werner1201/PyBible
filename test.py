from pypager.source import GeneratorSource
from pypager.pager import Pager
from prompt_toolkit.token import ZeroWidthEscape
import io


def generate_a_lot_of_content():
    """
    This is a function that generates content on the fly.
    It's called when the pager needs to display more content.
    """
    # counter = 0
    # while counter < 10:
    #     yield [(counter, 'line: %i\n' % counter)]
    #     counter += 1
    output = io.StringIO(newline="\n")
    output.write("Primeira Linha")
    output.write("Segunda Linha")
    return output


if __name__ == '__main__':
    source = GeneratorSource(generate_a_lot_of_content())
    p = Pager(source)
    p.run()
