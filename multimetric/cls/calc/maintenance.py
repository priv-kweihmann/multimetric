import math  # noqa: F401

from multimetric.cls.base_calc import MetricBaseCalc


class MetricBaseCalcMaintenanceIndex(MetricBaseCalc):

    MI_DEFAULT = "classic"

    METRIC_MAINTAINABILITY_INDEX = "maintainability_index"

    @staticmethod
    def _mi_sei(metrics):
        try:
            res = 171.0 - (5.2 * math.log2(metrics["halstead_volume"]))
            res -= (0.23 * metrics["cyclomatic_complexity"])
            res -= (16.2 * math.log2(metrics["loc"]))
            res += (50.0 * abs(math.sin(math.sqrt(2.4 * metrics["comment_ratio"]))))
            return res
        except ValueError:  # pragma: no cover
            return 0  # pragma: no cover

    @staticmethod
    def _mi_microsoft(metrics):
        try:
            res = 171.0
            res -= (5.2 * math.log(metrics["halstead_volume"]))
            res -= (0.23 * metrics["cyclomatic_complexity"])
            res -= (16.2 * math.log(metrics["loc"]) * 100.0 / 171.0)
            return max(0, res)
        except ValueError:
            return 0

    @staticmethod
    def _mi_classic(metrics):
        try:
            res = 171.0
            res -= (5.2 * math.log(metrics["halstead_volume"]))
            res -= (0.23 * metrics["cyclomatic_complexity"])
            res -= (16.2 * math.log(metrics["loc"]))
            return max(0, res)
        except ValueError:  # pragma: no cover
            return 0  # pragma: no cover

    MI_METHOD = {
        "sei": _mi_sei,
        "classic": _mi_microsoft,
        "microsoft": _mi_classic,
    }

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self.__miMethod = args.maintenance_index_calc_method

    def get_results(self, metrics):
        metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX] = MetricBaseCalcMaintenanceIndex.MI_METHOD[self.__miMethod](
            metrics)
        # Sanity
        metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX] = max(
            metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX], 0)
        metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX] = min(
            metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX], 100)
        return super().get_results(metrics)
