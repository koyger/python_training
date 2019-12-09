# -*- coding: utf-8 -*-
import random
import string
from model.group import Group

constant = [
    Group(name="Group name 1", header="Header 1", footer="Footer 1"),
    Group(name="Group name 2", header="Header 2", footer="Footer 2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("Group ", 10), header=random_string("Header ", 12), footer=random_string("Footer ", 12))
    for i in range(2)
]

