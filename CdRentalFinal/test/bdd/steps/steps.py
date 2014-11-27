# -*- coding: utf-8 -*-
from lettuce import * 
from nose.tools import assert_equal
from webtest import TestApp
from cdrental_app import app

@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)
    assert_equal(world.response.text, u'Hello World!')

 
