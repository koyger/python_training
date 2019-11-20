# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    contact_to_add = User(first_name="User first name", last_name="User last name", company_name="center2m", address="User street, 21")
    app.open_home_page()
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact_to_add)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_to_add)
    assert sorted(old_contacts, key=User.id_or_max) == sorted(new_contacts, key=User.id_or_max)


def test_add_user_with_empty_fields(app):
    contact_to_add = User(first_name="", last_name="", company_name="", address="")
    app.open_home_page()
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact_to_add)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_to_add)
    assert sorted(old_contacts, key=User.id_or_max) == sorted(new_contacts, key=User.id_or_max)