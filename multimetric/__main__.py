import argparse
import json
import os
import textwrap
import sys

import chardet
from pygments import lexers

from multimetric.cls.importer.filtered import FilteredImporter
from multimetric.cls.importer.pick import importer_pick
from multimetric.cls.modules import get_additional_parser_args
from multimetric.cls.modules import get_modules_calculated
from multimetric.cls.modules import get_modules_metrics
from multimetric.cls.modules import get_modules_stats


def ArgParser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        prog="multimetric", description='Calculate code metrics in various languages',
        epilog=textwrap.dedent("""
        Currently you could import files of the following types for --warn_* or --coverage

        Following information can be read

            <file> = full path to file
            <content> = either a string
            <severity> = optional severity

            Note: you could also add a single line, then <content>
                has to be a number reflecting to total number of findings

        File formats

        csv: CSV file of following line format
             <file>,<content>,<severity>

        json: JSON file
             <file>: {
                 "content": <content>,
                 "severity": <severity>
             }
        """))
    parser.add_argument(
        "--warn_compiler",
        help="File(s) holding information about compiler warnings")
    parser.add_argument(
        "--warn_duplication",
        help="File(s) holding information about code duplications")
    parser.add_argument(
        "--warn_functional",
        help="File(s) holding information about static code analysis findings")
    parser.add_argument(
        "--warn_standard",
        help="File(s) holding information about language standard violations")
    parser.add_argument(
        "--warn_security",
        help="File(s) File(s) holding information about found security issue")
    parser.add_argument(
        "--coverage",
        help="File(s) with compiler warningsFile(s) holding information about testing coverage")
    get_additional_parser_args(parser)
    parser.add_argument("files", nargs='+', help="Files to parse")
    RUNARGS = parser.parse_args()
    # Turn all paths to abs-paths right here
    RUNARGS.files = [os.path.abspath(x) for x in RUNARGS.files]
    return RUNARGS


if __name__ == '__main__':
    _args = ArgParser()
    _result = {"files": {}, "overall": {}}

    # Get importer
    _importer = {}
    _importer["import_compiler"] = importer_pick(_args, _args.warn_compiler)
    _importer["import_coverage"] = importer_pick(_args, _args.coverage)
    _importer["import_duplication"] = importer_pick(
        _args, _args.warn_duplication)
    _importer["import_functional"] = importer_pick(
        _args, _args.warn_functional)
    _importer["import_security"] = importer_pick(_args, _args.warn_standard)
    _importer["import_standard"] = importer_pick(_args, _args.warn_security)

    # instance metric modules
    _overallMetrics = get_modules_metrics(_args, **_importer)
    _overallCalc = get_modules_calculated(_args, **_importer)

    for f in _args.files:
        try:
            _lexer = lexers.get_lexer_for_filename(f)
            _result["files"][f] = {}
            with open(f, "rb") as i:
                _cnt = i.read()
                _enc = chardet.detect(_cnt)
                _cnt = _cnt.decode(_enc["encoding"]).encode("utf-8")
            _localImporter = {k: FilteredImporter(
                v, f) for k, v in _importer.items()}
            tokens = list(_lexer.get_tokens(_cnt))
            _localMetrics = get_modules_metrics(_args, **_localImporter)
            _localCalc = get_modules_calculated(_args, **_localImporter)
            for x in _localMetrics:
                x.parse_tokens(_lexer.name, tokens)
                _result["files"][f].update(x.get_results())
            for x in _overallMetrics:
                x.parse_tokens(_lexer.name, tokens)
                _result["overall"].update(x.get_results())
            for x in _localCalc:
                _result["files"][f].update(
                    x.get_results(_result["files"][f]))
        except UnicodeDecodeError as e:
            print(str(e))
    for x in _overallCalc:
        _result["overall"].update(x.get_results(_result["overall"]))
    for m in get_modules_stats(_args, **_importer):
        _result = m.get_results(_result, "files", "overall")

    # Output
    print(json.dumps(_result, indent=2, sort_keys=True))
