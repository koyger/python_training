from fixture.db import DbFixture
from fixture.orm import ORMFixture
import pymysql.cursors

db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for one in l:
        print(one)
    print(len(l))
finally:
    pass
    # db.destroy()


