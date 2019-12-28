from multimetric.cls.base import MetricBase


class MetricBaseLOC(MetricBase):
    _needles = [
        "Token.Text"
    ]
    _contents = [
        '\n',
        '\r\n'
    ]

    METRIC_LOC = "loc"

    def __init__(self, args):
        super().__init__(args)

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        if not any(tokens):
            # to avoid a log(0) the minimum of loc is 1
            self._metrics[MetricBaseLOC.METRIC_LOC] = 1
        else:
            self._metrics[MetricBaseLOC.METRIC_LOC] = len([x for x in tokens if str(
                x[0]) in MetricBaseLOC._needles and x[1] in MetricBaseLOC._contents]) + 1
