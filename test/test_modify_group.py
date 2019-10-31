# -*- coding: utf-8 -*-
from model.group import *

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="X MODIFIED group", header="MODIFIED 11", footer="MODIFIED 22"))
    app.group.return_to_groups_page()
    app.session.logout()