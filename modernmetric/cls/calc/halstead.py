from modernmetric.cls.base_calc import MetricBaseCalc
from modernmetric.cls.metric.operands import MetricBaseOperands
from modernmetric.cls.metric.operators import MetricBaseOperator
import math


class MetricBaseCalcHalstead(MetricBaseCalc):

    BUGPRED_METHOD = {
        "old": "(self._effort * (2.0 / 3.0)) / 3000.0",
        "new": "self._volume / 3000.0"
    }

    BUGPRED_DEFAULT = "new"

    METRIC_HALSTEAD_VOLUME = "halstead_volume"
    METRIC_HALSTEAD_EFFORT = "halstead_effort"
    METRIC_HALSTEAD_DIFFICULTY = "halstead_difficulty"
    METRIC_HALSTEAD_BUGS = "halstead_bugprop"
    METRIC_HALSTEAD_TIMEREQ = "halstead_timerequired"

    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        try:
            self.__bugPredicMethod = args.halstead_bug_predict_method
        except AttributeError:
            self.__bugPredicMethod = MetricBaseCalcHalstead.BUGPRED_DEFAULT

    def _getNs(self, metrics):
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
        self._getNs(metrics)
        self._vocabulary = self._n1 + self._n2
        # to avoid a log(0) the minimum of vocabulary is 1
        self._vocabulary = max(1, self._vocabulary)
        return self._vocabulary

    def _getProgLength(self, metrics):
        self._getNs(metrics)
        self._length = self._N1 + self._N2
        return self._length

    def _getVolume(self, metrics):
        self._getVocabulary(metrics)
        self._getProgLength(metrics)
        self._volume = self._length * math.log2(self._vocabulary)
        # to avoid a log(0) the minimum of volume is 1
        self._volume = max(1, self._volume)
        return self._volume

    def _getDifficulty(self, metrics):
        self._getNs(metrics)
        self._difficulty = (self._n1 / 2.0) * (self._N2 / self._n2)
        return self._difficulty

    def _getEffort(self, metrics):
        self._getVolume(metrics)
        self._getDifficulty(metrics)
        self._effort = self._volume * self._difficulty
        return self._effort

    def _getTime(self, metrics):
        self._getEffort(metrics)
        self._timeRequired = self._effort / 18.0
        return self._timeRequired

    def _getBug(self, metrics):
        self._getEffort(metrics)
        self._bug = eval(MetricBaseCalcHalstead.BUGPRED_METHOD[self.__bugPredicMethod])
        return self._bug

    def get_results(self, metrics):
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_VOLUME] = self._getVolume(metrics)
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_DIFFICULTY] = self._getDifficulty(metrics)
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_EFFORT] = self._getEffort(metrics)
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_TIMEREQ] = self._getTime(metrics)
        metrics[MetricBaseCalcHalstead.METRIC_HALSTEAD_BUGS] = self._getBug(metrics)
        return super().get_results(metrics)
