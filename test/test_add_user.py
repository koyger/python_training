# -*- coding: utf-8 -*-
import pytest
from fixture.application import *
from model.user import *

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(User(first_name="User first name", last_name="User last name", company_name="center2m", address="User street, 21"))
    app.session.logout()

def test_add_user_with_empty_fields(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(User(first_name="", last_name="", company_name="", address=""))
    app.session.logout()