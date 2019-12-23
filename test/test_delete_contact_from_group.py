# -*- coding: utf-8 -*-
import random
import time
from model.group import Group
from model.user import Contact


def test_delete_contact_from_group(app, orm_db):
    # удаляем несколько связей для компенсации
    for n in range(4):
        app.open_home_page()
        group_db_id = None
        user_to_remove_id = None
        groups = app.group.groups_without_empty_names(orm_db.get_group_list())
        len_before = len(groups)
        # почистим список групп
        for gr in range(len_before):
            # remove groups without contacts
            if len(orm_db.get_contacts_in_group(groups[len_before-gr-1])) == 0:
                groups.pop(len_before-gr-1)
        # если после чистки коннектов не осталось, ниже процесс создания коннекта
        if len(groups) == 0:
            # если совсем пользователей нет, добавим
            if app.contact.count() == 0:
                app.contact.create(Contact(firstname="t_a_c_t_g User first name", lastname="t_a_c_t_g User last name",
                                           companyname="t_a_c_t_g user center2m", address="t_a_c_t_g User street, 21", id=None))
            # если групп с непустыми именами совсем нет, добавим
            if len(app.group.groups_without_empty_names(orm_db.get_group_list())) == 0:
                app.group.create(Group(name="t_a_c_t_g group", header="11 first group", footer="22 first group"))
                # теперь можно добавить хотя бы одного пользователя в случайную группа
            groups = app.group.groups_without_empty_names(orm_db.get_group_list())
            group = random.choice(groups)
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
                if ui_id == user_to_add.id:
                    index = c
            app.contact.add_to_group(index, group_db_id)
        # Проверки закончены, коннект точно есть. Берем случайную группу и удаляем любой контакт
        groups = app.group.groups_without_empty_names(orm_db.get_group_list())
        # почистим список групп
        len_before = len(groups)
        for gr in range(len_before):
            # remove groups without contacts
            if len(orm_db.get_contacts_in_group(groups[len_before - gr - 1])) == 0:
                # print("GROUP NAME WITHOUT CONNs = " + groups[len_before-gr-1].name)
                groups.pop(len_before - gr - 1)
        gr_ind = random.randrange(len(groups))
        group_del_conn = groups[gr_ind]
        filtered_contact_list = orm_db.get_contacts_in_group(group_del_conn)
        count = len(filtered_contact_list)
        index = random.randrange(count)
        # функция возвращает ID удаленного из группы юзера
        contact_deleted_id = app.contact.remove_user_from_group(group_del_conn.id, index)
        group_db_id = group_del_conn.id
        user_to_remove_id = contact_deleted_id
        cont_list_after = orm_db.get_contacts_in_group(Group(id=group_db_id))
        # ищем id удаленного контакта в группе
        for u in range(len(cont_list_after)):
            if cont_list_after[u].id == user_to_remove_id:
                assert False
        # если не нашли, порядок
        assert True




