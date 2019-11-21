# -*- coding: utf-8 -*-
from model.group import *


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group_to_add = Group(name="New group", header="11", footer="22")
    app.group.create(group_to_add)
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_to_add)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_with_empty_fields(app):
    old_groups = app.group.get_group_list()
    group_to_add = Group(name="", header="", footer="")
    app.group.create(group_to_add)
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_to_add)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
