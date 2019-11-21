# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []  # удалили первый элемент
    assert old_groups == new_groups

# второй тест на удаление группы добавлен для баланса, чтобы не копились группы бесконечно
def test_delete_first_group_2(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []  # удалили первый элемент
    assert old_groups == new_groups
