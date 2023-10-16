# SPDX-FileCopyrightText: 2023 Konrad Weihmann
# SPDX-License-Identifier: Zlib

import math

from multimetric.cls.base_calc import MetricBaseCalc
from multimetric.cls.metric.operands import MetricBaseOperands
from multimetric.cls.metric.operators import MetricBaseOperator


class MetricBaseCalcHalstead(MetricBaseCalc):
    """A class for calculating Halstead metrics.

    This class inherits from MetricBaseCalc.

    Attributes
    ----------
    METRIC_HALSTEAD_VOLUME : str
        The name of the Halstead volume metric.
    METRIC_HALSTEAD_EFFORT : str
        The name of the Halstead effort metric.
    METRIC_HALSTEAD_DIFFICULTY : str
        The name of the Halstead difficulty metric.
    METRIC_HALSTEAD_BUGS : str
        The name of the Halstead bugprop metric.
    METRIC_HALSTEAD_TIMEREQ : str
        The name of the Halstead timerequired metric.

    Methods
    -------
    _bugpred_old(obj)
        Calculate the bug prediction using the old method.
    _bugpred_new(obj)
        Calculate the bug prediction using the new method.
    _getNs(metrics)
        Calculate the values of N1, N2, n1, n2.
    _getVocabulary(metrics)
        Calculate the vocabulary of the program.
    _getProgLength(metrics)
        Calculate the program length.
    _getVolume(metrics)
        Calculate the Halstead volume.
    _getDifficulty(metrics)
        Calculate the Halstead difficulty.
    _getEffort(metrics)
        Calculate the Halstead effort.
    _getTime(metrics)
        Calculate the time required.
    _getBug(metrics)
        Calculate the bugprop.
    get_results(metrics)
        Calculate all the Halstead metrics and return the results.

    """

    METRIC_HALSTEAD_VOLUME = "halstead_volume"
    METRIC_HALSTEAD_EFFORT = "halstead_effort"
    METRIC_HALSTEAD_DIFFICULTY = "halstead_difficulty"
    METRIC_HALSTEAD_BUGS = "halstead_bugprop"
    METRIC_HALSTEAD_TIMEREQ = "halstead_timerequired"

    @staticmethod
    def _bugpred_old(obj):
        """Calculate the bug prediction using the old method.

        Parameters
        ----------
        obj : MetricBaseCalcHalstead
            The MetricBaseCalcHalstead object.

        Returns
        -------
        float
            The bug prediction using the old method.

        """
        return (obj._effort * (2.0 / 3.0)) / 3000.0

    @staticmethod
    def _bugpred_new(obj):
        """Calculate the bug prediction using the new method.

        Parameters
        ----------
        obj : MetricBaseCalcHalstead
            The MetricBaseCalcHalstead object.

        Returns
        -------
        float
            The bug prediction using the new method.

        """
        return obj._volume / 3000.0

    BUGPRED_DEFAULT = "new"
    BUGPRED_METHOD = {
        "old": _bugpred_old,
        "new": _bugpred_new,
    }

    def __init__(self, args, **kwargs):
        """Initialize the MetricBaseCalcHalstead object.

        Parameters
        ----------
        args : argparse.Namespace
            The command line arguments.
        **kwargs
            Additional keyword arguments.

        """
        super().__init__(args, **kwargs)
        self.__bugPredicMethod = args.halstead_bug_predict_method

    def _getNs(self, metrics):
        """Calculate the values of N1, N2, n1, n2.

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Notes
        -----
        - N1 is the total number of operators
        - N2 is the total number of operands
        - n1 is the number of distinct operators
        - n2 is the number of distinct operands
        """
        self._N2 = float(metrics[MetricBaseOperands.METRIC_OPERANDS_SUM])
        self._N1 = float(metrics[MetricBaseOperator.METRIC_OPERATORS_SUM])
        self._n2 = float(metrics[MetricBaseOperands.METRIC_OPERANDS_UNIQUE])
        self._n1 = float(metrics[MetricBaseOperator.METRIC_OPERATORS_UNIQUE])
        # to avoid any Divbyzero bugs set the minimum to 1
        self._n1 = max(self._n1, 1)
        self._n2 = max(self._n2, 1)
        self._N1 = max(self._N1, 1)
        self._N2 = max(self._N2, 1)

    def _getVocabulary(self, metrics):
        """Calculate the vocabulary of the program.

        Halstead vocabulary (n) is defined as the sum of distinct
        operators and operands. (n1 + n2)

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        float
            The vocabulary of the program.

        """
        self._getNs(metrics)
        self._vocabulary = self._n1 + self._n2
        # to avoid a log(0) the minimum of vocabulary is 1
        self._vocabulary = max(1, self._vocabulary)
        return self._vocabulary

    def _getProgLength(self, metrics):
        """Calculate the program length.

        Halstead program length (N) is defined as the sum of total
        operators and operands. (N1 + N2).

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        float
            The program length.

        """
        self._getNs(metrics)
        self._length = self._N1 + self._N2
        return self._length

    def _getVolume(self, metrics):
        """Calculate the Halstead volume.

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        float
            The Halstead volume.

        """
        self._getVocabulary(metrics)
        self._getProgLength(metrics)
        self._volume = self._length * math.log2(self._vocabulary)
        # to avoid a log(0) the minimum of volume is 1
        self._volume = max(1, self._volume)
        return self._volume

    def _getDifficulty(self, metrics):
        """Calculate the Halstead difficulty.

        The difficulty measure is related to the difficulty of the program
        to write or understand, e.g. when doing code review.

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        float
            The Halstead difficulty.

        """
        self._getNs(metrics)
        self._difficulty = (self._n1 / 2.0) * (self._N2 / self._n2)
        return self._difficulty

    def _getEffort(self, metrics):
        """Calculate the Halstead effort.

        The effort measure translates into actual coding time.

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        float
            The Halstead effort.

        """
        self._getVolume(metrics)
        self._getDifficulty(metrics)
        self._effort = self._volume * self._difficulty
        return self._effort

    def _getTime(self, metrics):
        """Calculate the estimated time required to write program.

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        float
            The time required to write the program, in seconds.

        """
        self._getEffort(metrics)
        self._timeRequired = self._effort / 18.0
        return self._timeRequired

    def _getBug(self, metrics):
        """Calculate the estimate for the number of errors in the implementation.

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        float
            The number of delivered bugs.
        """
        self._getEffort(metrics)
        self._bug = MetricBaseCalcHalstead.BUGPRED_METHOD[self.__bugPredicMethod](self)
        return self._bug

    def get_results(self, metrics):
        """Calculate all the Halstead metrics and return the results.

        Parameters
        ----------
        metrics : dict
            The metrics dictionary.

        Returns
        -------
        dict
            The metrics dictionary with the Halstead metrics added.

        """
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_VOLUME] = self._getVolume(
            metrics
        )
        metrics[
            MetricBaseCalcHalstead.METRIC_HALSTEAD_DIFFICULTY
        ] = self._getDifficulty(metrics)
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_EFFORT] = self._getEffort(
            metrics
        )
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_TIMEREQ] = self._getTime(metrics)
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_BUGS] = self._getBug(metrics)
        return super().get_results(metrics)
