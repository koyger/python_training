from sys import maxsize


class User:

    def __init__(self, first_name=None, last_name=None, company_name=None,
                 address=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and \
               self.last_name == other.last_name and \
               self.first_name == other.first_name

    def id_or_max(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize
