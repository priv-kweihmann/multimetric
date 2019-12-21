from multimetric.cls.metric import CalcMetric

import math  # noqa: F401


class MaintenanceIndex(CalcMetric):

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

    def __init__(self, args):
        super().__init__(args)
        try:
            self.__miMethod = args.maintenance_index_calc_method
        except AttributeError:
            self.__miMethod = MaintenanceIndex.MI_DEFAULT

    def get_results(self, metrics):
        metrics["maintainability_index"] = eval(
            MaintenanceIndex.MI_METHOD[self.__miMethod])
        # Sanity
        metrics["maintainability_index"] = max(
            metrics["maintainability_index"], 0)
        metrics["maintainability_index"] = min(
            metrics["maintainability_index"], 100)
        return super().get_results(metrics)
