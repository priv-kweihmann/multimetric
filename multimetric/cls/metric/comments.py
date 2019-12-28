from multimetric.cls.base import MetricBase


class MetricBaseComments(MetricBase):
    _needles = [
        "Token.Comment",
        "Token.Comment.Hashbang",
        "Token.Comment.Multiline",
        "Token.Comment.Preproc",
        "Token.Comment.Single",
        "Token.Comment.Special",
        "Token.Literal.String.Doc"
    ]

    METRIC_COMMENT_RATIO = "comment_ratio"

    def __init__(self, args):
        super().__init__(args)
        self.__overall = 0
        self.__comments = 0

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        for x in tokens:
            self.__overall += len(str(x[1]))
            if str(x[0]) in MetricBaseComments._needles:
                self.__comments += len(str(x[0]))

    def get_results(self):
        if self.__overall == 0:
            # sanity
            self.__overall = 1
        self._metrics[MetricBaseComments.METRIC_COMMENT_RATIO] = self.__comments * \
            100.0 / float(self.__overall)
        return self._metrics
