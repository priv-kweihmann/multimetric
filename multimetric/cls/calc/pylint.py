# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib
from multimetric.cls.base_calc import MetricBaseCalc
from multimetric.cls.metric.operators import MetricBaseOperator
from multimetric.cls.metric.operands import MetricBaseOperands


class MetricBaseCalcPylint(MetricBaseCalc):

    METRIC_PYLINT = "pylint"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self.__addArgs = kwargs

    def __getFromImporter(self, section, severity, _default=0.0):
        if f"import_{section}" in self.__addArgs:
            return self.__addArgs[f"import_{section}"].getSumItems(
                _filter={"severity": severity},
            )
        return _default

    def __getError(self, metrics):
        return (self.__getFromImporter("compiler", "error") +
                self.__getFromImporter("functional", "error") +
                self.__getFromImporter("standard", "error") +
                self.__getFromImporter("security", "error")) * 5.0

    def __getWarning(self, metrics):
        return (self.__getFromImporter("compiler", "warning") +
                self.__getFromImporter("functional", "warning") +
                self.__getFromImporter("standard", "warning") +
                self.__getFromImporter("security", "warning"))

    def __getInfo(self, metrics):
        return (self.__getFromImporter("compiler", "info") +
                self.__getFromImporter("functional", "info") +
                self.__getFromImporter("standard", "info") +
                self.__getFromImporter("security", "info"))

    def __getScore(self, metrics):
        _statements = (metrics[MetricBaseOperands.METRIC_OPERANDS_SUM] +
                       metrics[MetricBaseOperator.METRIC_OPERATORS_SUM]) or 1.0
        return max(100.0 - ((float(self.__getError(metrics) +
                                   self.__getWarning(metrics) +
                                   self.__getInfo(metrics)) /
                            _statements) * 100.0), 0.0)

    def get_results(self, metrics):
        metrics[MetricBaseCalcPylint.METRIC_PYLINT] = self.__getScore(metrics)
        return super().get_results(metrics)
