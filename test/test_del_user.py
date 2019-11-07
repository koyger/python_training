# -*- coding: utf-8 -*-

def test_del_first_user(app):
    app.contact.delete_first()
