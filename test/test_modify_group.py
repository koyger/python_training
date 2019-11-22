# -*- coding: utf-8 -*-
from model.group import *
from random import randrange


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    old_groups = app.group.get_group_list()
    group_to_modify = Group(name="X MODIFIED group", header="MODIFIED 11", footer="MODIFIED 22")
    index = randrange(len(old_groups))
    group_to_modify.id = old_groups[index].id
    app.group.modify_group_by_index(group_to_modify, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    # вписываем модифицированную группу в первый элемент списка old_group
    old_groups[index] = group_to_modify
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    old_groups = app.group.get_group_list()
    group_to_modify = Group(name="X MODIFIED NAME only group")
    index = randrange(len(old_groups))
    group_to_modify.id = old_groups[index].id
    app.group.modify_group_by_index(group_to_modify, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    # вписываем модифицированную группу в первый элемент списка old_group
    old_groups[index] = group_to_modify
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)