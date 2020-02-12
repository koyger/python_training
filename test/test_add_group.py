# -*- coding: utf-8 -*-
import allure
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group_data = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add a group {} to the list'.format(group_data.name)):
        app.group.create(group_data)
        app.group.open_groups_page()
    with allure.step('Then the new group is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group_data)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
