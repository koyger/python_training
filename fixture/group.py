from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def fill_group(self, group):
        self.app.change_field_value("group_name", group.name)
        self.app.change_field_value("group_header", group.header)
        self.app.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        self.group_cache = None

    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.open_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def count(self):
        # quantity of groups
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select group
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
