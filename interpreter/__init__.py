import interpreter.parser as p
import interpreter.ast
import interpreter.environment
import pprint


def execute(source, show_ast: bool=False, disable_warnings: bool=True):
    p.disable_warnings = disable_warnings

    res = p.get_parser().parse(source)

    environment.declare_env(interpreter.ast.symbols)

    for node in res.children:
        node.eval()

    if show_ast:
        print("\n\n" + '=' * 80, ' == Syntax tree ==')

        pp = pprint.PrettyPrinter()
        pp.pprint(res.children)
        pp.pprint(interpreter.ast.symbols.table())