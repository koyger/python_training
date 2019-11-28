from model.user import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact(self, contact):
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("company", contact.companyname)
        self.app.change_field_value("address", contact.address)

    def create(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(user)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contacts_cache = None

    def open_user_to_edit_by_index(self, user, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.user_line_selected(index).find_element_by_xpath(".//img[@alt='Edit']").click()
        self.fill_contact(user)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contacts_cache = None

    def open_user_view_by_index(self, user, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.user_line_selected(index).find_element_by_xpath(".//img[@alt='Details']").click()

    def user_line_selected(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        return wd.find_elements_by_name("entry")[index]

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.user_line_selected(index).find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contacts_cache = None

    def count(self):
        # quantity of contacts
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("entry"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                all_phones = cells[5].text.splitlines()
                # print(all_phones[0]+" "+all_phones[1]+" "+all_phones[2])
                scanned_contact = Contact(firstname=firstname, lastname=lastname, id=id, homephone=all_phones[0], mobilephone=all_phones[1], workphone=all_phones[2])
                self.contacts_cache.append(scanned_contact)
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, i_of_u):
        wd = self.app.wd
        self.user_line_selected(i_of_u).find_element_by_xpath(".//img[@alt='Edit']").click()
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone)



