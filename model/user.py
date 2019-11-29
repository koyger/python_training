from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, companyname=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_homepage=None,
                 email1=None, email2=None, email3=None, all_emails_from_homepage=None):
        self.firstname = firstname
        self.lastname = lastname
        self.companyname = companyname
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage

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
