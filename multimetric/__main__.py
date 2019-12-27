from pygments import lexers
from multimetric.cls.calc_halstead import Halstead
from multimetric.cls.calc_maintenance import MaintenanceIndex
from multimetric.cls.metric_comments import CommentsMetric
from multimetric.cls.metric_cyclomatic import CyclomaticComplexity
from multimetric.cls.metric_loc import LOCMetric
from multimetric.cls.metric_operands import OperandsMetric
from multimetric.cls.metric_operators import OperatorMetric
from multimetric.cls.calc_average import Average

import argparse
import json
import os


def ArgParser():
    parser = argparse.ArgumentParser(
        prog="multimetric", description='Calculate code metrics in various languages')
    parser.add_argument("--bugpredict", choices=Halstead.BUGPRED_METHOD.keys(), default=Halstead.BUGPRED_DEFAULT,
                        help="Method how to calculate the bug prediction", dest="halstead_bug_predict_method")
    parser.add_argument("--maintindex", choices=MaintenanceIndex.MI_METHOD.keys(), default=MaintenanceIndex.MI_DEFAULT,
                        help="Method how to calculate the maintainability index", dest="maintenance_index_calc_method")
    parser.add_argument("files", nargs='+', help="Files to parse")
    RUNARGS = parser.parse_args()
    # Turn all paths to abs-paths right here
    RUNARGS.files = [os.path.abspath(x) for x in RUNARGS.files]
    return RUNARGS


if __name__ == '__main__':
    _args = ArgParser()
    _result = {"files": {}, "overall": {}}
    _overallMetrics = [LOCMetric(_args), CommentsMetric(_args), OperandsMetric(
        _args), OperatorMetric(_args), CyclomaticComplexity(_args)]
    _overallCalc = [Halstead(_args), MaintenanceIndex(_args)]

    for f in _args.files:
        with open(f) as i:
            try:
                _lexer = lexers.get_lexer_for_filename(f)
                _result["files"][f] = {}
                tokens = list(_lexer.get_tokens(i.read()))
                _localMetrics = [LOCMetric(_args), CommentsMetric(_args), OperandsMetric(
                    _args), OperatorMetric(_args), CyclomaticComplexity(_args)]
                _localCalc = [Halstead(_args), MaintenanceIndex(_args)]
                for x in _localMetrics:
                    x.parse_tokens(_lexer.name, tokens)
                    _result["files"][f].update(x.get_results())
                for x in _overallMetrics:
                    x.parse_tokens(_lexer.name, tokens)
                    _result["overall"].update(x.get_results())
                for x in _localCalc:
                    _result["files"][f].update(x.get_results(_result["files"][f]))
            except UnicodeDecodeError:
                pass
    for x in _overallCalc:
        _result["overall"].update(x.get_results(_result["overall"]))
    _result = Average(_args).get_results(_result, "files", "overall")
    print(json.dumps(_result, indent=2, sort_keys=True))
