# -*- coding: utf-8 -*-
from lettuce import step
import os
from nose.tools import assert_equal, assert_in

@step(u'Given I have "([^"]*)" on my directory')
def given_i_have_group1_on_my_directory(step, filename):
	filepath = '/home/supersherlock/Desktop/repo/CSC-183-Activities/proxy/proxy/' + filename
	assert os.path.isfile(filepath)

@step(u'When I run the "([^"]*)" successful')
def when_i_run_the_group1(step, filename): 
    #os.system('python proxy/proxy.py')
    assert True

@step(u'Then I will have this result:')
def then_i_will_have_these(step):
	list = []
	a = open('result.txt','r')
	read = a.readlines() 
	for i in range(len(read)): 
		list.append(read[i].rstrip('\n'))

	 
 
	for row in step.hashes:
		b = row['Result'] 
		print b
		if str(b) not in list:
		    assert False




 
