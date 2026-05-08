import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from antlr4 import CommonTokenStream, FileStream
from generated.FormGenLexer import FormGenLexer
from generated.FormGenParser import FormGenParser


def test_tokens(filepath):
    print("=" * 50)
    print("TOKENS")
    print("=" * 50)

    input_stream = FileStream(filepath, encoding='utf-8')
    lexer = FormGenLexer(input_stream)

    stream = CommonTokenStream(lexer)
    stream.fill()

    for token in stream.tokens:
        if token.type != -1:
            name = FormGenLexer.symbolicNames[token.type] \
                   if token.type < len(FormGenLexer.symbolicNames) \
                   else "EOF"
            print(f"  [{token.line:>3}:{token.column:<3}]  {name:<20}  {repr(token.text)}")


def test_parse(filepath):
    print()
    print("=" * 50)
    print("ÁRBOL DE SINTAXIS")
    print("=" * 50)

    input_stream = FileStream(filepath, encoding='utf-8')
    lexer = FormGenLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FormGenParser(stream)

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() == 0:
        print("  ✅ Sin errores de sintaxis")
        print()
        print(tree.toStringTree(recog=parser))
    else:
        print(f"  ❌ {parser.getNumberOfSyntaxErrors()} error(es) de sintaxis")


if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'examples/registro_empleado.fg'
    test_tokens(filepath)
    test_parse(filepath)