# -*- coding: utf-8 -*-
from model.group import *

def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="X MODIFIED group", header="MODIFIED 11", footer="MODIFIED 22"))

def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="X MODIFIED NAME group"))
    # ЛОГАУТ ДЛЯ ПРОВЕРКИ ИНТЕЛЛЕКТУАЛЬНОГО ЛОГИНА, ПОСЛЕ ПРОВЕРКИ УБРАТЬ !!!
    app.session.logout()

def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="MODIFIED HEADER"))
