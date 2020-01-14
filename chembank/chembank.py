
from json import dump, load, dumps
from os.path import exists, isfile, join
from os import makedirs, listdir

from .experiment import Experiment

class DataType():
    experiments = 0
    chemicals = 1

class DiskDBNode(object):
    def __init__(self, rootdir, nodename):
        self.rootdir = rootdir
        self.nodedir = join(rootdir, nodename)
        self.indexfile = join(self.rootdir, "{}-index".format(nodename))
        self.indexes = {}
        if not exists(self.nodedir):
            makedirs(self.nodedir)
        if not isfile(self.indexfile):
            with open(self.indexfile, 'w') as f:
                f.write(self.new_index)
        with open(self.indexfile, 'r') as f:
            for line in f.readline():
                field, indexname = line.split("\t")
                self.indexes[field]=indexname

    @property
    def new_index(self):
        return """"""

    def _json_read(self, filename):
        with open(filename, 'r') as _handle:
            return load(_handle)

    def get_object(self, identifier):
        object_location = join(self.nodedir, identifier)
        if not exists(object_location):
            return
        data = self._json_read(object_location)
        data['identifier'] = identifier
        return data

    def _resolve_identifiers(self, identifiers):
        return [self.get_object(id) for id in identifiers]

    def list(self):
        return self._resolve_identifiers(
            [ d for d in listdir(self.nodedir) if isfile(join(self.nodedir, d)) ]
        )


    def _indexed(self, field, query):
        pass

    def search(self, field, query):
        if field in self.indexes:
            return self._indexed(field, query)
        matches = []
        for obj in self.list():
            if str(query).lower() in str(obj[field]).lower():
                matches.append(obj)
        return matches

class ChemBank(object):
    def __init__(self, datadir):
        self.datadir = datadir
        self.experiment_node = DiskDBNode(rootdir=datadir, nodename="experiments")

    def list_experiments(self):
        return self.experiment_node.list()

    def search_experiments(self, field, query):
        self.experiment_node.search(field, query)
