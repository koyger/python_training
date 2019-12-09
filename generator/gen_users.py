# -*- coding: utf-8 -*-
import jsonpickle
import os
import random
import string
import getopt
import sys
from model.user import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(dig_len):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(dig_len)])


testdata = [Contact(firstname="", lastname="", companyname="", address="")] + [
    Contact(firstname=random_string("First_Name ", 10), lastname=random_string("Last_Name ", 10),
            companyname=random_string("Company ", 20), address=random_string("Address ", 20),
            email1="random@email.com",  # correct email parametrization is a bit complex thing
            homephone="+1(323)" + random_digits(7), mobilephone="+1(323)" + random_digits(7), workphone="+1(323)" + random_digits(7))
    for i in range(n)
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file_path, "w") as f_out:
    jsonpickle.set_encoder_options("json", indent=2)
    f_out.write(jsonpickle.encode(testdata))
