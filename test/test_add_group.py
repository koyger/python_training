# -*- coding: utf-8 -*-
import pytest
from fixture.application import *
from model.group import *

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="New group", header="11", footer="22"))
    app.session.logout()

def test_add_group_with_empty_fields(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
