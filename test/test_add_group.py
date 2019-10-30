# -*- coding: utf-8 -*-
from model.group import *

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="New group", header="11", footer="22"))
    app.group.return_to_groups_page()
    app.session.logout()

def test_add_group_with_empty_fields(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()
