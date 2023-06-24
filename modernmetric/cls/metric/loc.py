from modernmetric.cls.base import MetricBase


class MetricBaseLOC(MetricBase):
    METRIC_LOC = "loc"

    _needles = [
        "Token.Text"
    ]

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        self._metrics[MetricBaseLOC.METRIC_LOC] = 0
        for x in tokens:
            if str(x[0]) in MetricBaseLOC._needles:
                self._metrics[MetricBaseLOC.METRIC_LOC] += len([y for y in x[1] if y == '\n'])
        self._metrics[MetricBaseLOC.METRIC_LOC] = max(self._metrics[MetricBaseLOC.METRIC_LOC], 1)
        self._internalstore["loc"] = self._metrics[MetricBaseLOC.METRIC_LOC]

    def get_results_global(self, value_stores):
        _sum = sum([x["loc"] for x in self._get_all_matching_store_objects(value_stores)])
        return { MetricBaseLOC.METRIC_LOC: _sum }