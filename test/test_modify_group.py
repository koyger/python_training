# -*- coding: utf-8 -*-
from model.group import *


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    app.group.modify_first_group(Group(name="X MODIFIED group", header="MODIFIED 11", footer="MODIFIED 22"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    app.group.modify_first_group(Group(name="X MODIFIED NAME group"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
    app.group.modify_first_group(Group(header="MODIFIED HEADER"))
