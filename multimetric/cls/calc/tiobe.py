# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
import math

from multimetric.cls.base_calc import MetricBaseCalc
from multimetric.cls.metric.cyclomatic import MetricBaseCyclomaticComplexity
from multimetric.cls.metric.fanout import MetricBaseFanout
from multimetric.cls.metric.loc import MetricBaseLOC


class MetricBaseCalcTIOBE(MetricBaseCalc):

    METRIC_TIOBE_COVERAGE = "tiobe_coverage"
    METRIC_TIOBE_FUNCTIONAL = "tiobe_functional"
    METRIC_TIOBE_COMPLEXITY = "tiobe_complexity"
    METRIC_TIOBE_COMPILER = "tiobe_compiler"
    METRIC_TIOBE_STANDARD = "tiobe_standard"
    METRIC_TIOBE_DUPLICATION = "tiobe_duplication"
    METRIC_TIOBE_FANOUT = "tiobe_fanout"
    METRIC_TIOBE_SECURITY = "tiobe_security"
    METRIC_TIOBE = "tiobe"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self.__addArgs = kwargs

    def __getScaledValue(self, metrics, value):
        try:
            return 100.0 / ((value) / (metrics[MetricBaseLOC.METRIC_LOC] / 1000.0) + 1.0)
        except ZeroDivisionError:
            return 0.0

    def __getFromImporter(self, section, _default=0.0):
        if f"import_{section}" in self.__addArgs:
            return self.__addArgs[f"import_{section}"].getSumItems()
        return _default

    def __getTiobeComplexity(self, metrics):
        cc = metrics[MetricBaseCyclomaticComplexity.METRIC_CYCLOMATIC_COMPLEXITY]
        return 6400.0 / float(math.pow(cc, 3) - math.pow(cc, 2) - cc + 65)

    def __getTiobeFanout(self, metrics):
        _int = metrics[MetricBaseFanout.METRIC_FANOUT_INTERNAL]
        _ext = metrics[MetricBaseFanout.METRIC_FANOUT_EXTERNAL]
        return float(min(max(120.0 - ((8.0 * _int) + (2.0 * _ext)), 0.0), 100.0))

    def __getTiobeCoverage(self, metrics):
        _per = max(0.0, self.__getFromImporter("coverage", _default=100.0))
        return min(((0.75 * _per) + 32.5), 100.0)

    def __getTiobeStandard(self, metrics):
        return self.__getScaledValue(metrics, self.__getFromImporter("standard"))

    def __getTiobeSecurity(self, metrics):
        return self.__getScaledValue(metrics, self.__getFromImporter("security"))

    def __getTiobeDuplication(self, metrics):
        return min(-30.0 * math.log10(self.__getFromImporter("duplication") or 0.00001) +
                   70.0, 100.0)

    def __getTiobeCompiler(self, metrics):
        _violations = self.__getScaledValue(metrics, self.__getFromImporter("compiler"))
        return max(100.0 - 50.0 *
                   math.log((101 - _violations) or 0.00001), 0.0)

    def __getTiobeFunctional(self, metrics):
        _violations = self.__getFromImporter("functional")
        return max(self.__getScaledValue(metrics, _violations) * 2.0 - 100.0, 0.0)

    def __getTiobe(self, metrics):
        return ((metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_COVERAGE] * 0.2) +
                (metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_FUNCTIONAL] * 0.2) +
                (metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_COMPLEXITY] * 0.15) +
                (metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_COMPILER] * 0.15) +
                (metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_STANDARD] * 0.1) +
                (metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_DUPLICATION] * 0.1) +
                (metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_FANOUT] * 0.05) +
                (metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_SECURITY] * 0.05))

    def get_results(self, metrics):
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_COMPLEXITY] = self.__getTiobeComplexity(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_FANOUT] = self.__getTiobeFanout(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_COMPILER] = self.__getTiobeCompiler(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_COVERAGE] = self.__getTiobeCoverage(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_DUPLICATION] = self.__getTiobeDuplication(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_FUNCTIONAL] = self.__getTiobeFunctional(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_SECURITY] = self.__getTiobeSecurity(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE_STANDARD] = self.__getTiobeStandard(metrics)
        metrics[MetricBaseCalcTIOBE.METRIC_TIOBE] = self.__getTiobe(metrics)
        return super().get_results(metrics)
