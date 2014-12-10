# -*- coding: utf-8 -*-
from lettuce import * 
from nose.tools import assert_equal,assert_in
from webtest import TestApp
from cd.cds import *
from cd.cd import *
from cd.customer import *
from cd.customers import *
from cdrental_app import app

 
# cds = minidictionary.cds
# customers = minidictionary.customers
# # class minidictionary(object):
# # 	def __init__(self):
# # 	    self.cds = Cds()
# # 	    self.customers = Customers()

@step(u'I visit the homepage')
def i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200) 

@step(u'When I input customer id "([^"]*)" and cd id "([^"]*)"')
def when_i_input_customer_id_group1_and_cd_id_group2(step, customer_id, cd_id):
    form = world.response.forms['checkout']
    form['customer_id'] = customer_id
    form['cd_id'] = cd_id
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200) 

 
@step(u'I see output "([^"]*)"')
def then_i_see_output_group1(step, output):
    assert_in ("Output: {}".format(output), world.form_response.text)

@step(u'Given I have the following cds:')
def given_i_have_the_following_cds(step):
    for row in step.hashes:
        cd = Cd(row['cd_id'], row['title'],row['isrented'],row['rentedBy'])
        Cds().add_cd(cd) 

@step(u'And I have the following listed customers:')
def and_i_have_the_following_listed_customers(step): 
    for row in step.hashes:
        customer = Customer(row['customer_id'], row['name'],row['rented'],row['rentedArray'])
        Customers().add_customer(customer) 

 
 
