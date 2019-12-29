class Importer():

    class ImporterItem():

        def __init__(self, _file, _cnt, _sev):
            self._values = {
                "filename": _file,
                "content": _cnt,
                "severity": _sev
            }

        def match(self, _filter):
            return all([self._values[k] == v for k, v in _filter.items()])

        def get(self):
            return self._values

        @staticmethod
        def from_csv(line):
            _sev = None
            if len(line) > 2:
                _sev = line[2]
            return Importer.ImporterItem(_file=line[0], _cnt=line[1], _sev=_sev)

    def __init__(self, args, filearg):
        self._input = filearg
        self._items = []

    def getItems(self, _filter={}):
        return [x.get() for x in self._items if x.match(_filter)]

    def getSumItems(self, _filter={}):
        _items = self.getItems(_filter=_filter)
        if len(_items) == 1:
            if str.isdigit(_items[0]["content"]):
                return int(_items[0]["content"])
        return len(_items)
