# -*- coding: utf-8 -*-
import jsonpickle
import os
import random
import string
import getopt
import sys
from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("Group ", 10), header=random_string("Header ", 12), footer=random_string("Footer ", 12))
    for i in range(n)
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file_path, "w") as f_out:
    jsonpickle.set_encoder_options("json", indent=2)
    f_out.write(jsonpickle.encode(testdata))
