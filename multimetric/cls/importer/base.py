class Importer():

    def __init__(self, args, filearg):
        self._input = filearg
        self._items = []

    def getItems(self, _filter=None):
        if _filter:
            return [x for x in self._items if x[0] == _filter]
        return self._items

    def getSumItems(self, _filter=None):
        _items = self.getItems(_filter=_filter)
        if len(_items) == 1:
            if str.isdigit(_items[0][1]):
                return int(_items[0][1])
        return len(_items)
