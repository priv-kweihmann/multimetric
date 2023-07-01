from multimetric.cls.base import MetricBase


class MetricBaseLOC(MetricBase):
    METRIC_LOC = "loc"

    _needles = [
        "Token.Text",
        "Token.Comment.Preproc",
        "Token.Text.Whitespace",
    ]

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self._previous_token = (None, None)

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        self._metrics[MetricBaseLOC.METRIC_LOC] = 0
        for x in tokens:
            if self._previous_token != x:
                if x[1].strip(' ').endswith('\n'):
                    self._metrics[MetricBaseLOC.METRIC_LOC] += 1
            self._previous_token = x
            
        self._metrics[MetricBaseLOC.METRIC_LOC] = max(self._metrics[MetricBaseLOC.METRIC_LOC], 1)
        self._internalstore["loc"] = self._metrics[MetricBaseLOC.METRIC_LOC]

    def get_results_global(self, value_stores):
        _sum = sum([x["loc"] for x in self._get_all_matching_store_objects(value_stores)])
        return {MetricBaseLOC.METRIC_LOC: _sum}
