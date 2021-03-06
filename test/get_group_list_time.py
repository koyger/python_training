from model.group import Group
from timeit import timeit


def get_group_list_time(app, db):
    # Test made to measure how quickly db.get works
    print("")
    print("FROM UI "+str(timeit(lambda: app.group.get_group_list(), number=1)))
    ui_list = app.group.get_group_list()
    print("FROM DB "+str(timeit(lambda: db.get_group_list(), number=1000)))
    db_list = db.get_group_list()
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)