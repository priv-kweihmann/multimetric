from multimetric.cls.metric import CalcMetric
import math


class Halstead(CalcMetric):

    BUGPRED_METHOD = {
        "old": "(self._effort * (2.0 / 3.0)) / 3000.0",
        "new": "self._volume / 3000.0"
    }

    BUGPRED_DEFAULT = "new"

    def __init__(self, args):
        super().__init__(args)
        try:
            self.__bugPredicMethod = args.halstead_bug_predict_method
        except AttributeError:
            self.__bugPredicMethod = Halstead.BUGPRED_DEFAULT

    def _getNs(self, metrics):
        self._N2 = float(metrics["operands_sum"])
        self._N1 = float(metrics["operators_sum"])
        self._n2 = float(metrics["operands_uniq"])
        self._n1 = float(metrics["operators_uniq"])

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
        self._bug = eval(Halstead.BUGPRED_METHOD[self.__bugPredicMethod])
        return self._bug

    def get_results(self, metrics):
        metrics["halstead_volume"] = self._getVolume(metrics)
        metrics["halstead_difficulty"] = self._getDifficulty(metrics)
        metrics["halstead_effort"] = self._getEffort(metrics)
        metrics["halstead_timerequired"] = self._getTime(metrics)
        metrics["halstead_bugprop"] = self._getBug(metrics)
        return super().get_results(metrics)
