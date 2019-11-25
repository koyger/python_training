# -*- coding: utf-8 -*-
from random import randrange
from model.user import User


def test_modify_first_user(app):
    if app.contact.count() == 0:
        app.contact.create(User(first_name="FIRST User first name", last_name="FIRST User last name", company_name="FIRST user center2m", address="FIRST User street, 21"))
    contact_to_modify = User(first_name="MODIFIED first name", last_name="X MODIFIED last name", company_name="MODIFIED center2m", address="MODIFIED street, 21")
    old_contacts = app.contact.get_contacts_list()
    index = 0
    contact_to_modify.id = old_contacts[index].id
    app.contact.modify_user_by_index(contact_to_modify, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # вписываем модифицированный контакт в выбранный элемент списка old_contacts
    old_contacts[index] = contact_to_modify
    assert sorted(old_contacts, key=User.id_or_max) == sorted(new_contacts, key=User.id_or_max)


def test_modify_some_user(app):
    if app.contact.count() == 0:
        app.contact.create(User(first_name="FIRST User first name", last_name="FIRST User last name", company_name="FIRST user center2m", address="FIRST User street, 21"))
    contact_to_modify = User(first_name="MODIFIED first name", last_name="X MODIFIED last name", company_name="MODIFIED center2m", address="MODIFIED street, 21")
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact_to_modify.id = old_contacts[index].id
    app.contact.modify_user_by_index(contact_to_modify, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    # вписываем модифицированный контакт в выбранный элемент списка old_contacts
    old_contacts[index] = contact_to_modify
    assert sorted(old_contacts, key=User.id_or_max) == sorted(new_contacts, key=User.id_or_max)
