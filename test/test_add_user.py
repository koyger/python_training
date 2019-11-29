# -*- coding: utf-8 -*-
from model.user import Contact


def test_add_user(app):
    contact_to_add = Contact(firstname="User first name", lastname="User last name", companyname="center2m", address="User street, 21",
                             email1="first@email.com",
                             homephone="+1(323)45555435", mobilephone="+1(888)6686786", workphone="+7(666)455535")
    app.open_home_page()
    old_contacts = app.contact.get_contacts_list_from_table()
    app.contact.create(contact_to_add)
    new_contacts = app.contact.get_contacts_list_from_table()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_to_add)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_user_with_empty_fields(app):
    contact_to_add = Contact(firstname="", lastname="", companyname="", address="")
    app.open_home_page()
    old_contacts = app.contact.get_contacts_list_from_table()
    app.contact.create(contact_to_add)
    new_contacts = app.contact.get_contacts_list_from_table()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_to_add)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)