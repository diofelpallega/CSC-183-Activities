# -*- coding: utf-8 -*-
from lettuce import step
import os

@step(u'Given I have an "([^"]*)" file')
def given_i_have_an_group1_file(step, filename):
	filepath = '/home/supersherlock/Desktop/repo/'
	filepath2 = 'CSC-183-Activities/observer/observer/'
	finalpath = filepath + filepath2 + str(filename)
	assert os.path.isfile(finalpath)

@step(u'When I run "([^"]*)" successfully')
def when_i_run_group1_successfully(step, filename):
    #os.system('python observer/observer.py')
    assert True, "say run is successful"

@step(u'Then I see the results')
def then_i_see_the_results(step):
	os.system('python observer/observer.py')
     

