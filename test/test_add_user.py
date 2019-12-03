# -*- coding: utf-8 -*-
import pytest
from model.user import Contact
import random
import string


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
    for i in range(3)
]


@pytest.mark.parametrize("contact_to_add", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, contact_to_add):
    app.open_home_page()
    old_contacts = app.contact.get_contacts_list_from_table()
    app.contact.create(contact_to_add)
    new_contacts = app.contact.get_contacts_list_from_table()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_to_add)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
