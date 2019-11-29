# -*- coding: utf-8 -*-
from model.user import Contact
from random import randrange


def test_del_some_user(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name", companyname="FIRST user center2m", address="FIRST User street, 21", id=None))
    old_contacts = app.contact.get_contacts_list_from_table()
    index = randrange(len(old_contacts))
    app.contact.delete_user_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list_from_table()
    old_contacts[index:index+1] = []  # убрали удаленный элемент из списка
    assert old_contacts == new_contacts
