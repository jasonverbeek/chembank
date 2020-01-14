from .dataformatter import DataFormatter

class Experiment(DataFormatter):
    def print(self):
        self.prn("{} [{}]".format(self.data['title'], self._date()))
        self.prn("\nRequired:")
        for item in self.data['required']:
            self.prn("\t- {}".format(item))
        self.prn("\nReplay:")
        for line in self.data['description']:
            self.prn(line)
        self.prn("\nTL;DR:")
        for step in self.data['tldr']:
            self.prn("\t- {}".format(step))


    def match(self, query):
        if not isinstance(query, str):
            raise Exception("argument query is supposed to be a str")
        query=query.lower()


