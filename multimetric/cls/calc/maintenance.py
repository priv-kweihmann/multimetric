from multimetric.cls.base_calc import MetricBaseCalc

import math  # noqa: F401


class MetricBaseCalcMaintenanceIndex(MetricBaseCalc):

    MI_METHOD = {
        "sei": '171.0 \
             - (5.2 * math.log2(metrics["halstead_volume"])) \
             - (0.23 * metrics["cyclomatic_complexity"]) \
             - (16.2 * math.log2(metrics["loc"])) \
             + (50.0 * math.sin(math.sqrt(2.4 * metrics["comment_ratio"])))',
        "classic": '171.0 \
            - (5.2 * math.log(metrics["halstead_volume"])) \
            - (0.23 * metrics["cyclomatic_complexity"]) \
            - (16.2 * math.log(metrics["loc"]))',
        "microsoft": 'max(0, \
                171.0 \
                - (5.2 * math.log(metrics["halstead_volume"])) \
                - (0.23 * metrics["cyclomatic_complexity"]), \
                - (16.2 * math.log(metrics["loc"]) * 100.0 / 171.0))'
    }

    MI_DEFAULT = "classic"

    METRIC_MAINTAINABILITY_INDEX = "maintainability_index"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        try:
            self.__miMethod = args.maintenance_index_calc_method
        except AttributeError:
            self.__miMethod = MetricBaseCalcMaintenanceIndex.MI_DEFAULT

    def get_results(self, metrics):
        try:
            metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX] = eval(
                MetricBaseCalcMaintenanceIndex.MI_METHOD[self.__miMethod])
        except Exception as e:
            metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX]=0
        # Sanity
        metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX] = max(
            metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX], 0)
        metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX] = min(
            metrics[MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX], 100)
        return super().get_results(metrics)
