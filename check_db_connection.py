from fixture.db import DbFixture
import pymysql.cursors

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for user in contacts:
        print(user)
    print(len(contacts))
finally:
    db.destroy()


