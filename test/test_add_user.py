# -*- coding: utf-8 -*-
import allure
from model.user import Contact


def test_add_user(app, db, json_contacts, check_ui):
    app.open_home_page()
    with allure.step('Given a contacts list'):
        old_contacts = db.get_contact_list()
    with allure.step('When I add a contact "{}" to the list'.format(json_contacts.firstname)):
        app.contact.create(json_contacts)
    with allure.step('Then contact "{}" exists in  the list'.format(json_contacts.firstname)):
        new_contacts = db.get_contact_list()
        old_contacts.append(json_contacts)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list_from_table(), key=Contact.id_or_max)

# THIS TEST IS LEFT FOR EDUCATIONAL PURPOSES
# def test_add_user_old(app, json_contacts):
#     app.open_home_page()
#     old_contacts = app.contact.get_contacts_list_from_table()
#     app.contact.create(json_contacts)
#     new_contacts = app.contact.get_contacts_list_from_table()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(json_contacts)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
