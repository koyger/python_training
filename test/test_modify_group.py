# -*- coding: utf-8 -*-
from model.group import *


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    old_groups = app.group.get_group_list()
    group_to_modify = Group(name="X MODIFIED group", header="MODIFIED 11", footer="MODIFIED 22")
    group_to_modify.id = old_groups[0].id
    app.group.modify_first_group(group_to_modify)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    # вписываем модифицированную группу в первый элемент списка old_group
    old_groups[0] = group_to_modify
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="X MODIFIED NAME group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="MODIFIED HEADER"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
