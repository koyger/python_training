# -*- coding: utf-8 -*-

def test_del_first_user(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()