# -*- coding: utf-8 -*-
import random
from fixture.orm import ORMFixture
from model.group import Group
from model.user import Contact


def test_add_contact_to_group(app, db):
    db_here = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")
    # создаем несколько связей
    for k in range(5):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name",
                                       companyname="FIRST user center2m", address="FIRST User street, 21", id=None))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        groups = db_here.get_group_list()
        group = random.choice(groups)
        group_db_id = group.id
        cont_list = db_here.get_contacts_not_in_group(Group(id=group_db_id))
        # если в выбранную группу все пользователи уже добавлены, создадим новую группу и
        # снова вызовем список непривязанных пользователей, он точно должен быть непустой
        if len(cont_list) == 0:
            app.group.create(Group(name="Group for a_c_t_g test", header="11 a_c_t_g test", footer="22 a_c_t_g test"))
            groups = db_here.get_group_list()
            group = random.choice(groups)
            group_db_id = group.id
            cont_list = db_here.get_contacts_not_in_group(Group(id=group_db_id))
        # print("")
        # print("GROUP CHOSEN = "+str(group))
        # выбираем случайного пользователя
        user_to_add = random.choice(cont_list)
        # let's specify the index of chosen user
        index = 0
        for c in range(len(cont_list)):
            ui_id = app.contact.find_user_id_by_index(c)
            # print(str(c)+" "+str(ui_id)+" "+str(user_to_add.id))
            if ui_id == user_to_add.id:
                index = c
        # print("USER ID = "+str(user_to_add.id)+",  INDEX = "+str(index))
        app.contact.add_to_group(index, group_db_id)
        # print("FULL USER TO ADD = "+str(user_to_add))
        cont_list_after = None
        cont_list_after = db_here.get_contacts_not_in_group(Group(id=group_db_id))
        app.open_home_page()
        # если контактов, не связанных с группой, нет, проверка не нужна - все уже правильно
        if cont_list_after is not None:
            # ищем id добавленного контакта среди недобавленных
            for u in range(len(cont_list_after)):
                if cont_list_after[u].id == user_to_add.id:
                    assert False
                assert True
        assert True




