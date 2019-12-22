# -*- coding: utf-8 -*-
import random
from model.group import Group
from model.user import Contact


def test_delete_contact_from_group(app, orm_db):
    # удаляем несколько связей для компенсации
    for n in range(2):
        # переместить эти добавления
        if len(orm_db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name",
                                       companyname="FIRST user center2m", address="FIRST User street, 21", id=None))
        if len(orm_db.get_group_list()) == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))

        app.open_home_page()
        group_db_id = None
        user_to_remove_id = None
        groups = orm_db.get_group_list()
        len_before = len(groups)
        # почистим список групп
        for gr in range(len_before):
            print("GR = "+str(gr))
            print("len_before-gr-1 = "+str(len_before-gr-1))
            print("GROUP NAME CHECKED = " + groups[len_before-gr-1].name)
            # remove groups with empty names
            if app.clear(groups[len_before-gr-1].name) == "":
                print("GROUP NAME CLEARED = " + groups[len_before-gr-1].name)
                groups.pop(len_before-gr-1)
            # remove groups without contacts
            if len(orm_db.get_contacts_in_group(groups[len_before-gr-1])) == 0:
                print("GROUP NAME WITHOUT CONNs = " + groups[len_before-gr-1].name)
                groups.pop(len_before-gr-1)
        # если список групп с коннектами нулевой, попробуем создать коннект для удаления
        if len(groups) == 0:
            pass
            # !!! ЗАПОЛНИТЬ

        # перемешаем подготовленный список групп, в каждой можно удалить связь
        random.shuffle(groups)
        # берем первую, то есть случайную, группу и удаляем любой контакт
        group_del_conn = groups[0]
        filtered_contact_list = orm_db.get_contacts_in_group(group_del_conn)
        count = len(filtered_contact_list)
        index = random.randrange(count)
        # функция возвращает ID удаленного из группы юзера
        contact_deleted_id = app.contact.remove_user_from_group(group_del_conn.id, index)
        group_db_id = group_del_conn.id
        user_to_remove_id = contact_deleted_id

        # if group_db_id is None or user_to_remove_id is None:
        #     # это значит, все группы пусты. добавить связь и дать айдишники группы и контакта для удаления связи
        #     group = random.choice(groups)
        #     group_db_id = group.id
        #     cont_list = orm_db.get_contacts_not_in_group(Group(id=group_db_id))
        #     # выбираем случайного пользователя
        #     user_to_add = random.choice(cont_list)
        #     # let's specify the index of chosen user
        #     index = None
        #     for c in range(len(cont_list)):
        #         ui_id = app.contact.find_user_id_by_index(c)
        #         if ui_id == user_to_add.id:
        #             index = c
        #             user_to_remove_id = ui_id
        #     app.contact.add_to_group(index, group_db_id)
        #     app.open_home_page()

        cont_list_after = None
        cont_list_after = orm_db.get_contacts_in_group(Group(id=group_db_id))
        app.open_home_page()
        # ищем id удаленного контакта в группе
        for u in range(len(cont_list_after)):
            if cont_list_after[u].id == user_to_remove_id:
                assert False
        # если не нашли, порядок
        assert True




