import pymysql.cursors
from model.group import Group
from model.user import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        gr_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (gr_id, name, header, footer) = row
                gr_list.append(Group(id=str(gr_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return gr_list

    def modify_group_by_id(self, id, group_data):
        gr_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor.fetchall():
                (gr_id, name, header, footer) = row
                gr_list.append(Group(id=str(gr_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return gr_list

    def get_contact_list(self):
        us_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, "
                           "address, home, mobile, work, "
                           "email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor.fetchall():
                (us_id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                us_list.append(Contact(id=str(us_id), firstname=firstname, lastname=lastname, address=address,
                                       homephone=home, mobilephone=mobile, workphone=work,
                                       email1=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return us_list

    def destroy(self):
        self.connection.close()
