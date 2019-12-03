# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.group import *


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=random_string("Group ", 10), header=random_string("Header ", 12), footer=random_string("Footer ", 12)),
    Group(name="", header="", footer="")
]


@pytest.mark.parametrize("group_data", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group_data):
    # pass
    old_groups = app.group.get_group_list()
    group_to_add = Group(name="New group", header="11", footer="22")
    app.group.create(group_to_add)
    app.group.open_groups_page()
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_to_add)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_group_with_empty_fields(app):
#     old_groups = app.group.get_group_list()
#     group_to_add = Group(name="", header="", footer="")
#     app.group.create(group_to_add)
#     app.group.open_groups_page()
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group_to_add)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
