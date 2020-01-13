
class DataFormatter(object):
    def __init__(self, data):
        self.data = data

    def _date(self):
        return self.data['date'][-1]
