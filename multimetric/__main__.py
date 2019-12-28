import argparse
import json
import os

from pygments import lexers

from multimetric.cls.modules import get_additional_parser_args
from multimetric.cls.modules import get_modules_calculated
from multimetric.cls.modules import get_modules_metrics
from multimetric.cls.modules import get_modules_stats


def ArgParser():
    parser = argparse.ArgumentParser(
        prog="multimetric", description='Calculate code metrics in various languages')
    get_additional_parser_args(parser)
    parser.add_argument("files", nargs='+', help="Files to parse")
    RUNARGS = parser.parse_args()
    # Turn all paths to abs-paths right here
    RUNARGS.files = [os.path.abspath(x) for x in RUNARGS.files]
    return RUNARGS


if __name__ == '__main__':
    _args = ArgParser()
    _result = {"files": {}, "overall": {}}
    _overallMetrics = get_modules_metrics(_args)
    _overallCalc = get_modules_calculated(_args)

    for f in _args.files:
        with open(f) as i:
            try:
                _lexer = lexers.get_lexer_for_filename(f)
                _result["files"][f] = {}
                tokens = list(_lexer.get_tokens(i.read()))
                _localMetrics = get_modules_metrics(_args)
                _localCalc = get_modules_calculated(_args)
                for x in _localMetrics:
                    x.parse_tokens(_lexer.name, tokens)
                    _result["files"][f].update(x.get_results())
                for x in _overallMetrics:
                    x.parse_tokens(_lexer.name, tokens)
                    _result["overall"].update(x.get_results())
                for x in _localCalc:
                    _result["files"][f].update(
                        x.get_results(_result["files"][f]))
            except UnicodeDecodeError:
                pass
    for x in _overallCalc:
        _result["overall"].update(x.get_results(_result["overall"]))
    for m in get_modules_stats(_args):
        _result = m.get_results(_result, "files", "overall")

    # Output
    print(json.dumps(_result, indent=2, sort_keys=True))
