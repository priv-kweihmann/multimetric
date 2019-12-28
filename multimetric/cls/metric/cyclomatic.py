from multimetric.cls.base import MetricBase


class MetricBaseCyclomaticComplexity(MetricBase):

    __exitPoints = [
        "return",
        "exit",
        "assert",
        "break",
        "continue",
        "yield"
    ]

    __conditions = [
        "if",
        "else",
        "elif",
        "case",
        "default",
        "for",
        "while",
        "and",
        "or",
        "&&",
        "||"
    ]

    METRIC_CYCLOMATIC_COMPLEXITY = "cyclomatic_complexity"

    def __init__(self, args):
        super().__init__(args)
        self.__conditions = 0
        self.__exitpoints = 0

    def parse_tokens(self, language, tokens):
        super().parse_tokens(language, [])
        for x in tokens:
            if str(x[1]) in MetricBaseCyclomaticComplexity.__exitPoints:
                self.__exitpoints += 1
            if str(x[1]) in MetricBaseCyclomaticComplexity.__conditions:
                self.__conditions += 1

    def get_results(self):
        self._metrics[MetricBaseCyclomaticComplexity.METRIC_CYCLOMATIC_COMPLEXITY] = max(
            self.__conditions - self.__exitpoints + 2, 0)
        return self._metrics
