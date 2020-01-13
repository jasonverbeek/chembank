from .dataformatter import DataFormatter

class Experiment(DataFormatter):
    def print(self):
        print("{} [{}]".format(self.data['title'], self._date()))
        print("\nRequired:")
        for item in self.data['required']:
            print("\t- {}".format(item))
        print("\nReplay:")
        for line in self.data['description']:
            print(line)
        print("\nTL;DR:")
        for step in self.data['tldr']:
            print("\t- {}".format(step))


    def match(self, query):
        if not isinstance(query, str):
            raise Exception("argument query is supposed to be a str")
        query=query.lower()
        

