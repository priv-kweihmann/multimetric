# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
from multimetric.cls.calc.halstead import MetricBaseCalcHalstead
from multimetric.cls.calc.maintenance import MetricBaseCalcMaintenanceIndex
from multimetric.cls.calc.pylint import MetricBaseCalcPylint
from multimetric.cls.calc.tiobe import MetricBaseCalcTIOBE
from multimetric.cls.metric.comments import MetricBaseComments
from multimetric.cls.metric.cyclomatic import MetricBaseCyclomaticComplexity
from multimetric.cls.metric.fanout import MetricBaseFanout
from multimetric.cls.metric.loc import MetricBaseLOC
from multimetric.cls.metric.operands import MetricBaseOperands
from multimetric.cls.metric.operators import MetricBaseOperator
from multimetric.cls.stats.stats import MetricBaseStatsAverage


def get_modules_metrics(args, **kwargs):
    return [
        MetricBaseComments(args, **kwargs),
        MetricBaseCyclomaticComplexity(args, **kwargs),
        MetricBaseFanout(args, **kwargs),
        MetricBaseLOC(args, **kwargs),
        MetricBaseOperands(args, **kwargs),
        MetricBaseOperator(args, **kwargs),
    ]


def get_modules_calculated(args, **kwargs):
    return [
        MetricBaseCalcHalstead(args, **kwargs),
        MetricBaseCalcMaintenanceIndex(args, **kwargs),
        MetricBaseCalcTIOBE(args, **kwargs),
        MetricBaseCalcPylint(args, **kwargs),
    ]


def get_modules_stats(args, **kwargs):
    return [
        MetricBaseStatsAverage(args, **kwargs),
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
    parser.add_argument("--maintindex-formula",
                        default="max(0,171.0 - 5.2 * math.log(halstead_volume) - 0.23* cyclomatic_complexity -16.2 * math.log(loc))",
                        help="Python Formula to calculate the maintainability index if individul is used, defaults to classic method",
                        dest="maintenance_index_calc_formula")
