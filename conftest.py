# -*- coding: utf-8 -*-
import pytest
from fixture.application import *

@pytest.fixture
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture