import pymysql.cursors
from model.group import Group


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

    def destroy(self):
        self.connection.close()
