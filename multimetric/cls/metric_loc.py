from multimetric.cls.metric import BaseMetric


class LOCMetric(BaseMetric):
    _needles = [
        "Token.Text"
    ]
    _contents = [
        '\n',
        '\r\n'
    ]

    def __init__(self, args):
        super().__init__(args)

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        if not any(tokens):
            # to avoid a log(0) the minimum of loc is 1
            self._metrics["loc"] = 1
        else:
            self._metrics["loc"] = len([x for x in tokens if str(
                x[0]) in LOCMetric._needles and x[1] in LOCMetric._contents]) + 1
