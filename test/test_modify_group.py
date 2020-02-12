# -*- coding: utf-8 -*-
import random

import allure
from model.group import Group
from data.groups import modgroupdata


def test_modify_groups(app, db, check_ui):
    for mod_gr in modgroupdata:
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        with allure.step('Given a list of groups'):
            group_to_modify = mod_gr
            old_groups = db.get_group_list()
            group = random.choice(old_groups)
        with allure.step('When you modify randomly chosen group "{}"'.format(group.name)):
            app.group.modify_group_by_id(group_to_modify, group.id)
            new_groups = db.get_group_list()
        with allure.step('Then new list of groups should be equal to old with chosen group modified'):
            # вписываем модифицированную группу в выбранный элемент списка old_group
            group.name = group_to_modify.name
            group.header = group_to_modify.header
            group.footer = group_to_modify.footer
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
            if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


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
