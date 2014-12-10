# -*- coding: utf-8 -*-
from lettuce import step
from nose.tools import assert_equal, assert_in
from facade.facade import *
import os

@step(u'Given I have the following:')
def given_i_have_the_following(step):
    for row in step.hashes: 
    	test = Test()
    	city = test.city
    	country = test.country
        assert_equal(city, row['city'])
        assert_equal(country, row['country'])	
 

@step(u'When I run the program')
def when_i_run_the_program(step):
    os.system('python facade.py')

@step(u'When I run the program')
def when_i_run_the_program(step):
    run = Run()
 

@step(u'Then I get the the following:')
def then_i_get_the_the_following(step):
    run = Run()
    forecast =  str(run.run())
    for row in step.hashes:
        what = row['forecast']
        assert_equal(forecast,what)

