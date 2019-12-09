# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.add_group import constant as testdata


@pytest.mark.parametrize("group_data", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group_data):
    old_groups = app.group.get_group_list()
    app.group.create(group_data)
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
