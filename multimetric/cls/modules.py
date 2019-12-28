from multimetric.cls.calc.halstead import MetricBaseCalcHalstead
from multimetric.cls.calc.maintenance import MetricBaseCalcMaintenanceIndex
from multimetric.cls.metric.comments import MetricBaseComments
from multimetric.cls.metric.cyclomatic import MetricBaseCyclomaticComplexity
from multimetric.cls.metric.fanout import MetricBaseFanout
from multimetric.cls.metric.loc import MetricBaseLOC
from multimetric.cls.metric.operands import MetricBaseOperands
from multimetric.cls.metric.operators import MetricBaseOperator
from multimetric.cls.stats.stats import MetricBaseStatsAverage
from multimetric.cls.calc.tiobe import MetricBaseCalcTIOBE


def get_modules_metrics(args):
    return [
        MetricBaseComments(args),
        MetricBaseCyclomaticComplexity(args),
        MetricBaseFanout(args),
        MetricBaseLOC(args),
        MetricBaseOperands(args),
        MetricBaseOperator(args),
    ]


def get_modules_calculated(args):
    return [
        MetricBaseCalcHalstead(args),
        MetricBaseCalcMaintenanceIndex(args),
        MetricBaseCalcTIOBE(args)
    ]


def get_modules_stats(args):
    return [
        MetricBaseStatsAverage(args)
    ]


def get_additional_parser_args(parser):
    parser.add_argument("--bugpredict",
                        choices=MetricBaseCalcHalstead.BUGPRED_METHOD.keys(),
                        default=MetricBaseCalcHalstead.BUGPRED_DEFAULT,
                        help="Method how to calculate the bug prediction",
                        dest="halstead_bug_predict_method")
    parser.add_argument("--maintindex",
                        choices=MetricBaseCalcMaintenanceIndex.MI_METHOD.keys(),
                        default=MetricBaseCalcMaintenanceIndex.MI_DEFAULT,
                        help="Method how to calculate the maintainability index",
                        dest="maintenance_index_calc_method")
