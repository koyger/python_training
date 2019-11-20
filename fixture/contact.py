from model.user import User


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact(self, contact):
        self.app.change_field_value("firstname", contact.first_name)
        self.app.change_field_value("lastname", contact.last_name)
        self.app.change_field_value("company", contact.company_name)
        self.app.change_field_value("address", contact.address)

    def create(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(user)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def modify_first(self, user):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(user)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def count(self):
        # quantity of contacts
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("entry"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            first_name = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(id) + ")]]/td[3]").text
            last_name = wd.find_element_by_xpath("//tr[.//input[contains(@value," + str(id) + ")]]/td[2]").text
            contacts.append(User(first_name=first_name, last_name=last_name, id=id))
        return contacts
