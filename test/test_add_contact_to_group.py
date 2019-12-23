# -*- coding: utf-8 -*-
import random
import time
from model.group import Group
from model.user import Contact


def test_add_contact_to_group(app, orm_db):
    # создаем несколько связей
    for k in range(4):
        app.open_home_page()
        groups = app.group.groups_without_empty_names(orm_db.get_group_list())
        # Уберем из списка группы, куда уже нельзя добавить юзеров
        for gr in range(len(groups)):
            len_before = len(groups)
            if len(orm_db.get_contacts_not_in_group(groups[len_before-gr-1])) == 0:
                print("GROUP NAME FULL WITH CONNs = " + groups[len_before-gr-1].name)
                groups.pop(len_before-gr-1)
        # если после чистки групп с возможностью коннекта не осталось, добавим юзера
        if len(groups) == 0:
            app.contact.create(Contact(firstname="t_a_c_t_g User", lastname="t_a_c_t_g User last name",
                                       companyname="t_a_c_t_g user center2m", address="t_a_c_t_g User street, 21"))
            # если групп с непустыми названиями совсем нет, добавим группу и опять очистим
            groups = app.group.groups_without_empty_names(orm_db.get_group_list())
            if len(groups) == 0:
                app.group.create(Group(name="t_a_c_t_g Group"))
                groups = app.group.groups_without_empty_names(orm_db.get_group_list())
        print("КОЛИЧЕСТВО ГРУПП ПОСЛЕ = " + str(len(groups)))
        # теперь во все группы из groups можно добавить хотя бы одного пользователя, поэтому выберем случайную
        group = random.choice(groups)
        print("GROUP CHOSEN FOR ADDING NAME= " + group.name)
        print("GROUP CHOSEN FOR ADDING ID = " + group.id)
        group_db_id = group.id
        cont_of_gr_list = orm_db.get_contacts_not_in_group(Group(id=group_db_id))
        # выбираем случайного пользователя
        user_to_add = random.choice(cont_of_gr_list)
        # let's specify the index of chosen user
        index = None
        app.wd.get(app.base_url + "group.php")
        time.sleep(1)
        app.open_home_page()
        time.sleep(1)
        for c in range(len(cont_of_gr_list)):
            ui_id = app.contact.find_user_id_by_index(c)
            print("Пробуем юзер айди = "+str(ui_id)+" c user_to_add.id = "+str(user_to_add.id)+" по индексу "+str(c))
            if ui_id == user_to_add.id:
                index = c
                print("Подобран индекс = " + str(ui_id) + " для юзера с индексом " + str(index))

        print("попытка КОНТАКТ = " + str(index) + " ДОБАВЛЕН В ГРУППУ " + str(group_db_id))
        app.contact.add_to_group(index, group_db_id)
        print("!УСПЕХ! КОНТАКТ = " + str(index) + " ДОБАВЛЕН В ГРУППУ " + str(group_db_id))
        cont_list_after = None
        cont_list_after = orm_db.get_contacts_not_in_group(Group(id=group_db_id))
        # если контактов, не связанных с группой, нет, проверка не нужна - все уже правильно
        if cont_list_after is not None:
            # ищем id добавленного контакта среди недобавленных
            for u in range(len(cont_list_after)):
                if cont_list_after[u].id == user_to_add.id:
                    assert False
                assert True
        assert True




