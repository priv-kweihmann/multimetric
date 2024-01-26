# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib

import math

from multimetric.cls.base_calc import MetricBaseCalc


class MetricBaseCalcMaintenanceIndex(MetricBaseCalc):
    """Class for calculating the maintenance index metric.

    Attributes
    ----------
    MI_DEFAULT : str
        The default maintenance index calculation method.
    METRIC_MAINTAINABILITY_INDEX : str
        The name of the maintainability index metric.

    Methods
    -------
    _mi_sei(metrics)
        Calculate the maintenance index using the SEI method.
    _mi_microsoft(metrics)
        Calculate the maintenance index using the Microsoft method.
    _mi_classic(metrics)
        Calculate the maintenance index using the classic method.
    __init__(self, args, **kwargs)
        Initialize the MetricBaseCalcMaintenanceIndex object.
    get_results(self, metrics)
        Calculate the maintenance index metric and return the results.
    """

    MI_DEFAULT = "classic"
    METRIC_MAINTAINABILITY_INDEX = "maintainability_index"

    @staticmethod
    def _mi_sei(metrics):
        """Calculate the maintenance index using the SEI method.

        Parameters
        ----------
        metrics : dict
            The metrics used for calculation.

        Returns
        -------
        float
            The calculated maintenance index.

        Raises
        ------
        ValueError
            If any of the required metrics are missing.

        Notes
        -----
        The SEI maintainability index as published[1]_ is:

        171 - 5.2 * ln(aveV) - 0.23 * aveV(g’) - 16.2 * ln (aveLOC) - 50 * sin(sqrt(2.4 * perCM))

        where:
            - aveV = average Halstead Volume V per module
            - aveV(g’) = average extended cyclomatic complexity per module
            - aveLOC = the average count of lines of code (LOC) per module
            - perCM = average percent of lines of comments per module

        The result is returned as a float value, higher is better.

        References
        ----------
        .. [1] https://insights.sei.cmu.edu/documents/1625/1997_002_001_16523.pdf

        """
        try:
            res = 171.0 - (5.2 * math.log(metrics["halstead_volume"]))
            res -= 0.23 * metrics["cyclomatic_complexity"]
            res -= 16.2 * math.log(metrics["loc"])
            res += 50.0 * abs(math.sin(math.sqrt(2.4 * metrics["comment_ratio"])))
            return res
        except ValueError:  # pragma: no cover
            return 0  # pragma: no cover

    @staticmethod
    def _mi_microsoft(metrics):
        """Calculate the maintenance index using the Microsoft method.

        Parameters
        ----------
        metrics : dict
            The metrics used for calculation.

        Returns
        -------
        float
            The calculated maintenance index.

        Raises
        ------
        ValueError
            If any of the required metrics are missing.

        Notes
        -----
        This method uses the following formula to calculate the Microsoft maintenance index:

        MAX(0, (171 – 5.2 * ln(V) – 0.23 * CC – 16.2 * ln(LoC)) * 100 / 171)

        where:
            - V is the Halstead volume
            - CC is the cyclomatic complexity
            - LoC is the lines of code

        The result is returned as a float value, higher is better.

        Microsoft uses these thresholds[1]_.

        0-9 = Red
        10-19 = Yellow
        20-100 = Green

        References
        ----------
        .. [1] https://learn.microsoft.com/en-us/visualstudio/code-quality/code-metrics-maintainability-index-range-and-meaning?view=vs-2022
        """
        try:
            res = 171.0
            res -= 5.2 * math.log(metrics["halstead_volume"])
            res -= 0.23 * metrics["cyclomatic_complexity"]
            res -= 16.2 * math.log(metrics["loc"])
            res *= 100.0 / 171.0
            return max(0, res)
        except ValueError:
            return 0

    @staticmethod
    def _mi_classic(metrics):
        """Calculate the maintenance index using the classic method.

        Parameters
        ----------
        metrics : dict
            The metrics used for calculation.

        Returns
        -------
        float
            The calculated maintenance index.

        Raises
        ------
        ValueError
            If any of the required metrics are missing.

        Notes
        -----
        This method uses the following formula[1]_ to calculate the maintenance index:

        171 - 5.2 x ln(aveVol) - 0.23 x aveV(g’) - 16.2 x ln(aveLoC)

        where:
            - aveVol is average Halstead Volume
            - aveV(g’) is average extended cyclomatic complexity per module
            - aveLoC is average Lines Of Code

        The result is returned as a float value, higher is better.

        References
        ----------
        .. [1] https://learn.microsoft.com/en-us/visualstudio/code-quality/code-metrics-maintainability-index-range-and-meaning?view=vs-2022
        """
        try:
            res = 171.0
            res -= 5.2 * math.log(metrics["halstead_volume"])
            res -= 0.23 * metrics["cyclomatic_complexity"]
            res -= 16.2 * math.log(metrics["loc"])
            return max(0, res)
        except ValueError:  # pragma: no cover
            return 0  # pragma: no cover

    MI_METHOD = {
        "sei": _mi_sei,
        "classic": _mi_classic,
        "microsoft": _mi_microsoft,
    }

    def __init__(self, args, **kwargs):
        """Initialize the MetricBaseCalcMaintenanceIndex object.

        Parameters
        ----------
        args : argparse.Namespace
            The command line arguments.
        **kwarg
            Additional keyword arguments.

        Notes
        -----
        This method initializes the MetricBaseCalcMaintenanceIndex object by calling the
        __init__ method of the parent class (MetricBaseCalc) and setting the __miMethod attribute
        based on the value of args.maintenance_index_calc_method.
        """
        super().__init__(args, **kwargs)
        self.__miMethod = args.maintenance_index_calc_method

    def get_results(self, metrics):
        """Calculate the maintenance index metric and return the results.

        Parameters
        ----------
        metrics : dict
            The metrics used for calculation.

        Returns
        -------
        dict
            The updated metrics dictionary with the maintenance index metric.

        Notes
        -----
        This method calculates the maintenance index metric using the selected calculation method
        and updates the metrics dictionary with the result. The result is then clamped between 0 and 100.

        The updated metrics dictionary is returned.
        """
        metrics[
            MetricBaseCalcMaintenanceIndex.METRIC_MAINTAINABILITY_INDEX
        ] = MetricBaseCalcMaintenanceIndex.MI_METHOD[self.__miMethod](metrics)
        return super().get_results(metrics)
