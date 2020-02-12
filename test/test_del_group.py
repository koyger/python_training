# -*- coding: utf-8 -*-
import allure
from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    for i in range(2):
        with allure.step('Cycle {}.'.format(i+1)):
            if len(db.get_group_list()) == 0:
                app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        with allure.step('Given a list of groups'):
            old_groups = db.get_group_list()
            group = random.choice(old_groups)
        with allure.step('When I delete "{}" group'.format(group.name)):
            app.group.delete_group_by_id(group.id)
            new_groups = db.get_group_list()
            assert len(old_groups) - 1 == len(new_groups)
        with allure.step('Then old groups list equals new groups list plus deleted group'):
            old_groups.remove(group)
            assert old_groups == new_groups
            if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
