class FilteredImporter():
    def __init__(self, importer, filename):
        self.__importer = importer
        self.__filefilter = filename

    def getItems(self):
        return self.__importer.getItems({"filename": self.__filefilter})

    def getSumItems(self, _filter=None):
        return self.__importer.getSumItems(_filter={"filename": self.__filefilter, **(_filter or {})})
