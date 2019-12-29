class FilteredImporter():
    def __init__(self, importer, filename):
        self.__importer = importer
        self.__filefilter = filename

    def getItems(self):
        return self.__importer.getItems(_filter=self.__filefilter)

    def getSumItems(self, _filter=None):
        return self.__importer.getSumItems(_filter=self.__filefilter)