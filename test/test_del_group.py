# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_some_group(app, db):
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
#
# def test_delete_some_group(app):
#     for i in range(2):
#         if app.group.count() == 0:
#             app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
#         old_groups = app.group.get_group_list()
#         index = randrange(len(old_groups))
#         app.group.delete_group_by_index(index)
#         assert len(old_groups) - 1 == app.group.count()
#         new_groups = app.group.get_group_list()
#         old_groups[index:index+1] = []  # удалили первый элемент
#         assert old_groups == new_groups
