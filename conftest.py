# -*- coding: utf-8 -*-
import pytest
from fixture.application import *

@pytest.fixture
def app(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    request.addfinalizer(fixture.destroy)
    return fixture