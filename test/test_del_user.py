# -*- coding: utf-8 -*-
from model.user import User


def test_del_first_user(app):
    if app.contact.count() == 0:
        app.contact.create(User(first_name="FIRST User first name", last_name="FIRST User last name", company_name="FIRST user center2m", address="FIRST User street, 21"))
    app.contact.delete_first()
