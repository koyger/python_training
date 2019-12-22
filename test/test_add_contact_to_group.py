# -*- coding: utf-8 -*-
import random
from model.group import Group
from model.user import Contact


def test_add_contact_to_group(app, orm_db):
    # создаем несколько связей
    for k in range(4):
        app.open_home_page()
        groups = orm_db.get_group_list()
        len_before = len(groups)
        print("")
        print("КОЛИЧЕСТВО ГРУПП ДО = " + str(len_before))
        # Уберем из списка группы, куда уже нельзя добавить юзеров.Также группы с пустыми именами, из-за глюка с ними
        for gr in range(len_before):
            print("GR = "+str(gr))
            print("len_before-gr-1 = "+str(len_before-gr-1))
            print("GROUP NAME CHECKED = " + groups[len_before-gr-1].name)
            if app.clear(groups[len_before-gr-1].name) == "":
                print("GROUP NAME CLEARED = " + groups[len_before-gr-1].name)
                groups.pop(len_before-gr-1)
            if len(orm_db.get_contacts_not_in_group(groups[len_before-gr-1])) == 0:
                print("GROUP NAME FULL WITH CONNs = " + groups[len_before-gr-1].name)
                groups.pop(len_before-gr-1)
        # если после чистки групп не осталось (или не было до), добавим группу
        if len(groups) == 0:
            groups.append(Group(name="t_a_c_t_g group", header="11 first group", footer="22 first group"))
            # если добавлять в свежесозданную группу некого, значит совсем нет юзеров. Добавим юзера
            if orm_db.get_contacts_not_in_group(groups[0]) == 0:
                app.contact.create(Contact(firstname="t_a_c_t_g User", lastname="t_a_c_t_g User last name",
                                           companyname="t_a_c_t_g user center2m", address="t_a_c_t_g User street, 21",
                                           id=None))
        print("КОЛИЧЕСТВО ГРУПП ПОСЛЕ = " + str(len(groups)))
        # теперь во все группы из groups можно добавить хотя бы одного пользователя, поэтому выберем случайную
        group = random.choice(groups)
        print("GROUP CHOSEN FOR ADDING NAME= " + group.name)
        print("GROUP CHOSEN FOR ADDING ID = " + group.id)
        group_db_id = group.id
        cont_list = orm_db.get_contacts_not_in_group(Group(id=group_db_id))
        # выбираем случайного пользователя
        user_to_add = random.choice(cont_list)
        # let's specify the index of chosen user
        index = None
        for c in range(len(cont_list)):
            ui_id = app.contact.find_user_id_by_index(c)
            if ui_id == user_to_add.id:
                index = c
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




