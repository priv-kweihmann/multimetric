import os
import sys

from multimetric.cls.importer.base import Importer
from multimetric.cls.importer.mods.csv import ImporterCSV


def importer_pick(args, filearg):
    if not filearg:
        return Importer(args, None)
    _file, _ext = os.path.splitext(filearg)
    if _ext in [".csv"]:
        return ImporterCSV(args, filearg)
    sys.stderr.write("No supported importer found for {}\n".format(_ext))
    return Importer(args, None)
