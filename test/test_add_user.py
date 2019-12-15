# -*- coding: utf-8 -*-
from model.user import Contact


def test_add_user(app, db, json_contacts):
    app.open_home_page()
    old_contacts = db.get_contact_list()
    app.contact.create(json_contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# THIS TEST IS LEFT FOR EDUCATIONAL PURPOSES
# def test_add_user_old(app, json_contacts):
#     app.open_home_page()
#     old_contacts = app.contact.get_contacts_list_from_table()
#     app.contact.create(json_contacts)
#     new_contacts = app.contact.get_contacts_list_from_table()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(json_contacts)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
