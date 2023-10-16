from multimetric.cls.base import MetricBase


class MetricBaseCyclomaticComplexity(MetricBase):
    """A class for calculating cyclomatic complexity metric."""

    __exitPoints = [
        "return",
        "exit",
        "assert",
        "break",
        "continue",
        "yield",
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
        "||",
    ]

    METRIC_CYCLOMATIC_COMPLEXITY = "cyclomatic_complexity"

    def __init__(self, args, **kwargs):
        """Initialize the MetricBaseCyclomaticComplexity object.

        Parameters
        ----------
        args : list
            The arguments passed to the object.
        kwargs : dict
            The keyword arguments passed to the object.
        """
        super().__init__(args, **kwargs)
        self._internalstore["exitpoints"] = 0
        self._internalstore["conditions"] = 0

    def parse_tokens(self, language, tokens):
        """Parse the tokens and update the internal store.

        Parameters
        ----------
        language : str
            The language of the tokens.
        tokens : list
            The list of tokens to parse.
        """
        super().parse_tokens(language, [])
        for x in tokens:
            if str(x[1]) in MetricBaseCyclomaticComplexity.__exitPoints:
                self._internalstore["exitpoints"] += 1
            if str(x[1]) in MetricBaseCyclomaticComplexity.__conditions:
                self._internalstore["conditions"] += 1

    def get_results(self):
        """Calculate and return the metric results.

        Returns
        -------
        dict
            The metric results.
        """
        self._metrics[
            MetricBaseCyclomaticComplexity.METRIC_CYCLOMATIC_COMPLEXITY
        ] = max(
            self._internalstore["conditions"] - self._internalstore["exitpoints"] + 2, 0
        )
        return self._metrics

    def get_results_global(self, value_stores):
        """Calculate and return the global metric results.

        Parameters
        ----------
        value_stores : list
            The list of value stores.

        Returns
        -------
        dict
            The global metric results.
        """
        __exitPoints = 0
        __conditions = 0
        for x in self._get_all_matching_store_objects(value_stores):
            __conditions += x["conditions"]
            __exitPoints += x["exitpoints"]
        return {
            MetricBaseCyclomaticComplexity.METRIC_CYCLOMATIC_COMPLEXITY: max(
                __conditions - __exitPoints + 2, 0
            ),
        }
