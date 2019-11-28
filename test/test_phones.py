def test_phones_on_homepage(app):
    # проверяем первый контакт
    index = 0
    homepage_contact = app.contact.get_contacts_list()[index]
    print("HOMEPAGE CONTACT = "+str(homepage_contact))
    edit_page_contact = app.contact.get_contact_info_from_edit_page(index)
    print("EDIT PAGE CONTACT = "+str(edit_page_contact))
    assert homepage_contact.homephone == edit_page_contact.homephone
    assert homepage_contact.workphone == edit_page_contact.workphone
    assert homepage_contact.mobilephone == edit_page_contact.mobilephone
