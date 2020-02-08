

class BaseTableHeader(object):

    def __init__(self, text, value, align="center", sortable=False):
        self.text, self.value, self.align, self.sortable = text, value, align, sortable

