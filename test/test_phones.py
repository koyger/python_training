import random
import re
import allure


def test_phones_on_homepage(app):
    contact_list = app.contact.get_contacts_list_from_table()
    # задаем случайный номер контакта
    index = random.randrange(len(contact_list))
    homepage_contact = contact_list[index]
    edit_page_contact = app.contact.get_contact_info_from_edit_page(index)
    assert homepage_contact.all_phones_from_homepage == merge_phones_like_on_homepage(edit_page_contact)


def test_phones_on_contact_view_page(app):
    app.open_home_page()
    with allure.step('Given a list of contacts in UI table'):
        contact_list = app.contact.get_contacts_list_from_table()
        # задаем случайный номер контакта
        index = random.randrange(len(contact_list))
        viewpage_contact = app.contact.get_phones_info_from_view_page(index)
        app.open_home_page()
    with allure.step('When you take phone fields from edit page for a chosen contact "{}"'.format(viewpage_contact.firstname)):
        edit_page_contact = app.contact.get_contact_info_from_edit_page(index)
    with allure.step('Then phone fields from both sources should be equal'):
        assert viewpage_contact.homephone == edit_page_contact.homephone
        assert viewpage_contact.workphone == edit_page_contact.workphone
        assert viewpage_contact.mobilephone == edit_page_contact.mobilephone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))
