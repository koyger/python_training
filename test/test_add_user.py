# -*- coding: utf-8 -*-
from model.user import *

def test_add_user(app):
    app.contact.create(User(first_name="User first name", last_name="User last name", company_name="center2m", address="User street, 21"))
    app.session.logout()

def test_add_user_with_empty_fields(app):
    app.contact.create(User(first_name="", last_name="", company_name="", address=""))
    app.session.logout()