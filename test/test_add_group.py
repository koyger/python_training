# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    group_data = json_groups
    old_groups = db.get_group_list()
    app.group.create(group_data)
    app.group.open_groups_page()
    new_groups = db.get_group_list()
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
