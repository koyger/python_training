# -*- coding: utf-8 -*-
from model.user import Contact


def test_add_user(app, json_contacts):
    app.open_home_page()
    old_contacts = app.contact.get_contacts_list_from_table()
    app.contact.create(json_contacts)
    new_contacts = app.contact.get_contacts_list_from_table()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
