# -*- coding: utf-8 -*-
import random
from model.group import Group
from data.groups import modgroupdata


def test_modify_groups(app, db):
    for mod_gr in modgroupdata:
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        group_to_modify = mod_gr
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        app.group.modify_group_by_id(group_to_modify, group.id)
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        # вписываем модифицированную группу в выбранный элемент списка old_group
        group.name = group_to_modify.name
        group.header = group_to_modify.header
        group.footer = group_to_modify.footer
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# I LEAVE NON-DB UI FUNCTION FOR EDUCATIONAL PURPOSES
# def test_modify_some_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
#     old_groups = app.group.get_group_list()
#     group_to_modify = Group(name="12 DEC NAME only group")
#     index = randrange(len(old_groups))
#     group_to_modify.id = old_groups[index].id
#     app.group.modify_group_by_index(group_to_modify, index)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     # вписываем модифицированную группу в первый элемент списка old_group
#     old_groups[index] = group_to_modify
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
