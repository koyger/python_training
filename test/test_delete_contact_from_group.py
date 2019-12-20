# -*- coding: utf-8 -*-
import random
from model.group import Group
from model.user import Contact


def test_delete_contact_from_group(app, orm_db):
    # удаляем несколько связей для компенсации
    for n in range(2):
        if len(orm_db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name",
                                       companyname="FIRST user center2m", address="FIRST User street, 21", id=None))
        if len(orm_db.get_group_list()) == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        group_db_id = None
        user_to_remove_id = None
        groups = orm_db.get_group_list()
        # перемешаем список групп
        random.shuffle(groups)
        # перебираем группы до первой непустой
        for group in groups:
            contact_deleted_id = None
            filtered_contact_list = orm_db.get_contacts_in_group(Group(id=group.id))
            count = len(filtered_contact_list)
            if count != 0:
                index = random.randrange(count)
                contact_deleted_id = app.contact.remove_user_from_group(group.id, index)
                group_db_id = group.id
                user_to_remove_id = contact_deleted_id
                break

        if group_db_id is None or user_to_remove_id is None:
            # это значит, все группы пусты. добавить связь и дать айдишники группы и контакта для удаления связи
            group = random.choice(groups)
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
                    user_to_remove_id = ui_id
            app.contact.add_to_group(index, group_db_id)
            app.open_home_page()

        cont_list_after = None
        cont_list_after = orm_db.get_contacts_in_group(Group(id=group_db_id))
        app.open_home_page()
        # ищем id удаленного контакта в группе
        for u in range(len(cont_list_after)):
            if cont_list_after[u].id == user_to_remove_id:
                assert False
        # если не нашли, порядок
        assert True




