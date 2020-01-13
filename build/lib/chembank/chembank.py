
from json import dump, load, dumps
from os.path import exists, isfile, join
from os import makedirs

from .experiment import Experiment

class DataType():
    experiments = 0
    chemicals = 1

class ChemBank(object):
    def __init__(self, datadir):
        self.datadir = datadir

    def _ensure(self, datatype):
        """gives full path of datafile
           datatype can be one of:
               chembank.DataType.experiments or 0
               chembank.DataType.chemicals   or 1"""
        datafile = join(self.datadir, ['experiments', 'chemicals'][datatype]+".json")
        if not exists(self.datadir):
            makedirs(datadir)
        if not isfile(datafile):
            dump([], open(datafile, 'w'))
        return datafile

    def list_experiments(self):
        data = load(open(
            self._ensure(DataType.experiments),
            'r'))
        for exp in data:
            Experiment(exp).print()

    def list_chemicals(self):
        data = load(open(
            self._ensure(DataType.chemicals),
            'r'))
        for exp in data:
            print(dumps(exp, indent=4))
