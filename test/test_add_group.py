# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, data_groups):
    group_data = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group_data)
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
