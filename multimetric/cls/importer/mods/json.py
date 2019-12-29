import json
import sys

from multimetric.cls.importer.base import Importer


class ImporterJSON(Importer):

    def __init__(self, args, filearg):
        super().__init__(args, filearg)
        self.__readInput()

    def __readInput(self):
        try:
            with open(self._input) as i:
                reader = json.load(i)
                for k, v in reader.items():
                    _sev = None
                    if "severity" in v:
                        _sev = v["severity"]
                    self._items.append(Importer.ImporterItem(_file=k, _cnt=v["content"], _sev=_sev))
        except Exception as e:
            sys.stderr.write("Read error: {}\n".format(e))
