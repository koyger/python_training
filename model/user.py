from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, companyname=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.companyname = companyname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and \
               self.lastname == other.lastname and \
               self.firstname == other.firstname

    def id_or_max(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize
