# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import *

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="New group", header="11", footer="22"))
    app.logout()

def test_add_group_with_empty_fields(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
