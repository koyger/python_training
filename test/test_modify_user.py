# -*- coding: utf-8 -*-
from model.user import *

def test_modify_first_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(User(first_name="MODIFIED first name", last_name="MODIFIED last name", company_name="MODIFIED center2m", address="MODIFIED street, 21"))
    app.session.logout()