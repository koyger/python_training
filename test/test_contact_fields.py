import random
import re


def test_contact_fields_on_homepage(app):
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
