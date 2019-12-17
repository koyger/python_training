import random
import re


def test_contact_fields_on_homepage_vs_edit_page(app):
    contact_list = app.contact.get_contacts_list_from_table()
    # задаем случайный номер контакта
    index = random.randrange(len(contact_list))
    homepage_contact = contact_list[index]
    edit_page_contact = app.contact.get_contact_info_from_edit_page(index)
    assert clear(homepage_contact.firstname) == clear(edit_page_contact.firstname)
    assert clear(homepage_contact.lastname) == clear(edit_page_contact.lastname)
    assert clear(homepage_contact.address) == clear(edit_page_contact.address)
    assert homepage_contact.all_phones_from_homepage == merge_phones_like_on_homepage(edit_page_contact)
    assert homepage_contact.all_emails_from_homepage == merge_emails_like_on_homepage(edit_page_contact)


def test_all_contact_fields_on_homepage_vs_db(app, db):
    ui_contact_list = app.contact.get_contacts_list_from_table()
    db_contact_list = db.get_contact_list()
    print()
    contacts_count = len(ui_contact_list)
    index = random.randrange(contacts_count)
    # for index in range(contacts_count): ПОКА ОТКЛЮЧИЛ ЦИКЛ, БЕРУ СЛУЧАЙНЫЙ КОНТАКТ
    ui_contact = ui_contact_list[index]
    print("UI_CONTACT = "+str(ui_contact))
    db_id = int(app.contact.find_user_id_by_index(index))
    print("DB_ID = "+str(db_id))
    for k in range(contacts_count):
        k_contact = db_contact_list[k]
        if str(k_contact.id) == str(db_id):
            db_contact = k_contact
            print("DB_CONTACT = "+str(db_contact))
    assert clear(ui_contact.firstname) == clear(db_contact.firstname)
    assert clear(ui_contact.lastname) == clear(db_contact.lastname)
    assert clear(ui_contact.address) == clear(db_contact.address)
    assert ui_contact.all_phones_from_homepage == merge_phones_like_on_homepage(db_contact)
    assert ui_contact.all_emails_from_homepage == merge_emails_like_on_homepage(db_contact)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))
