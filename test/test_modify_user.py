# -*- coding: utf-8 -*-
from random import randrange
from model.user import Contact


def test_modify_first_user(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name", companyname="FIRST user center2m", address="FIRST User street, 21"))
    contact_to_modify = Contact(firstname="MODIFIED first name", lastname="X MODIFIED last name", companyname="MODIFIED center2m", address="MODIFIED street, 21",
                                homephone="+1(111)11-11111-11", mobilephone="+2(222)22-22-22", workphone="")
    old_contacts = app.contact.get_contacts_list()
    index = 0
    contact_to_modify.id = old_contacts[index].id
    app.contact.modify_user_by_index(contact_to_modify, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # вписываем модифицированный контакт в выбранный элемент списка old_contacts
    old_contacts[index] = contact_to_modify
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_some_user(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name", companyname="FIRST user center2m", address="FIRST User street, 21"))
    contact_to_modify = Contact(firstname="MODIFIED first name", lastname="X MODIFIED last name", companyname="MODIFIED center2m", address="MODIFIED street, 21",
                                homephone="+1(111)11-11111-11", mobilephone="", workphone="+3(333)33-33-33")
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact_to_modify.id = old_contacts[index].id
    app.contact.modify_user_by_index(contact_to_modify, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # вписываем модифицированный контакт в выбранный элемент списка old_contacts
    old_contacts[index] = contact_to_modify
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
