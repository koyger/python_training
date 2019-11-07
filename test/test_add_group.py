# -*- coding: utf-8 -*-
from model.group import *

def test_add_group(app):
    app.group.create(Group(name="New group", header="11", footer="22"))
    app.group.return_to_groups_page()

def test_add_group_with_empty_fields(app):
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
