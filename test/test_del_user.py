# -*- coding: utf-8 -*-
from model.user import User


def test_del_first_user(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(User(first_name="FIRST User first name", last_name="FIRST User last name", company_name="FIRST user center2m", address="FIRST User street, 21", id=None))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []  # удалили первый элемент
    assert old_contacts == new_contacts


