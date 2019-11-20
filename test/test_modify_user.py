# -*- coding: utf-8 -*-
from model.user import User


def test_modify_first_user(app):
    if app.contact.count() == 0:
        app.contact.create(User(first_name="FIRST User first name", last_name="FIRST User last name", company_name="FIRST user center2m", address="FIRST User street, 21"))
    contact_to_modify = User(first_name="MODIFIED first name", last_name="X MODIFIED last name", company_name="MODIFIED center2m", address="MODIFIED street, 21")
    old_contacts = app.contact.get_contacts_list()
    app.contact.modify_first(contact_to_modify)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    print("BEFORE insert contact_to_modify")
    print(old_contacts)
    # вписываем модифицированный контакт в первый элемент списка old_contacts
    old_contacts[0] = contact_to_modify
    print("AFTER insert contact_to_modify")
    print(old_contacts)
    print("NEW CONTACTS LIST")
    print(new_contacts)
    assert sorted(old_contacts, key=User.id_or_max) == sorted(new_contacts, key=User.id_or_max)
