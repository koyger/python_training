# -*- coding: utf-8 -*-
from model.user import *


def test_modify_first_user(app):
    if app.contact.count() == 0:
        app.contact.create(User(first_name="FIRST User first name", last_name="FIRST User last name", company_name="FIRST user center2m", address="FIRST User street, 21"))
    app.contact.modify_first(User(first_name="MODIFIED first name", last_name="X MODIFIED last name", company_name="MODIFIED center2m", address="MODIFIED street, 21"))
