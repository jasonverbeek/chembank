
import re

from .chemicals import Chemicals


variable_re = re.compile("\{\{([^\.]*)\.([^\}]*)\}\}")

variables = dict(chemical=Chemicals)

class DataFormatter(object):
    def __init__(self, data):
        self.data = data

    def _date(self):
        return self.data['date'][-1]

    def _return(self, line, test):
        return line if test else print(line)

    def _exists(self, category, key):
        cata = variables.get(category)
        return (cata and getattr(cata, key, None))

    def prn(self, line, test=False):
        vs = variable_re.findall(line)
        result = line
        for category, key in vs:
            if not self._exists(category, key):
                return self._return(line, test)
            value = getattr(variables[category], key)
            result = result.replace("{{%s.%s}}" % (category, key), value)
        return self._return(result, test)

