# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_some_group(app):
    for i in range(3):
        if app.group.count() == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        old_groups = app.group.get_group_list()
        index = randrange(len(old_groups))
        app.group.delete_group_by_index(index)
        assert len(old_groups) - 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[index:index+1] = []  # удалили первый элемент
        assert old_groups == new_groups
