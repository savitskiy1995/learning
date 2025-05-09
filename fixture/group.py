class GroupHelper:
    def __init__(self, app):
        self.app = app


    def test_add_group(self):
        wd = self.app.wd
        self.app.open_home_page(wd)
        self.app.create(wd)

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # path to edit form
        wd.find_element_by_name("edit").click()
        self.fill_group_form()
        # finishing group edit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field.name).click()
            wd.find_element_by_name(field.name).clear()
            wd.find_element_by_name(field.name).send_keys()

    def fill_group_form(self):
        wd = self.app.wd
        self.change_field_value("group.name", group.name)
        self.change_field_value("group.header", group.header)
        self.change_field_value("group.footer", group.footer)

    def change_field_value(self):
        if not group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys("group.name")

    def select_first_group(self):
        # select first group
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill in group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_element_by_name("selected[]"))

    def count_name_symbols(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        return len(wd.find_element_by_name("group_name"))
