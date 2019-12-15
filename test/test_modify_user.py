# -*- coding: utf-8 -*-
import random
from model.user import Contact
from data.contacts import moduserdata


def test_modify_some_user(app, db, check_ui):
    for mod_us in moduserdata:
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name",
                                       companyname="FIRST user center2m", address="FIRST User street, 21", id=None))
        old_contacts = db.get_contact_list()
        user = random.choice(old_contacts)
        mod_us.id = user.id
        index = None
        for c in range(len(old_contacts)):
            ui_id = app.contact.find_user_id_by_index(c)
            if ui_id == mod_us.id:
                index = c
        app.contact.modify_user_by_index(mod_us, index)
        new_contacts = db.get_contact_list()
        user.firstname = mod_us.firstname
        user.lastname = mod_us.lastname
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list_from_table(),
                                                                         key=Contact.id_or_max)


# I LEAVE THIS TEST FOR EDUCATIONAL PURPOSES
#
# def test_modify_some_user(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name", companyname="FIRST user center2m", address="FIRST User street, 21"))
#     contact_to_modify = Contact(firstname="MODIFIED first name", lastname="X MODIFIED last name", companyname="MODIFIED center2m", address="MODIFIED street, 21",
#                                 email3="third@email.com",
#                                 homephone="+1(111)11-11111-11", mobilephone="", workphone="+3(333)33-33-33")
#     old_contacts = app.contact.get_contacts_list_from_table()
#     index = randrange(len(old_contacts))
#     contact_to_modify.id = old_contacts[index].id
#     app.contact.modify_user_by_index(contact_to_modify, index)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contacts_list_from_table()
#     # вписываем модифицированный контакт в выбранный элемент списка old_contacts
#     old_contacts[index] = contact_to_modify
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
