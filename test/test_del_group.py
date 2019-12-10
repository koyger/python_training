# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    for i in range(2):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        app.group.delete_group_by_id(group.id)
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
