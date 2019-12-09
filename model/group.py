import re
from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        s_name = self.clear(self.name)
        o_name = self.clear(other.name)
        return (self.id is None or other.id is None or self.id == other.id) and s_name == o_name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize


    @staticmethod
    def clear(s):
        return re.sub("[() -]", "", s)