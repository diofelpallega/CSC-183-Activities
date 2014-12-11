# -*- coding: utf-8 -*-
from lettuce import step
import os

@step(u'Give I have a file named "([^"]*)"')
def give_i_have_a_file_named_group1(step, filename):
	filepath = '/home/supersherlock/Desktop/repo/'
	filepath2 = 'CSC-183-Activities/command/command/'
	finalpath  = filepath + filepath2 + filename
	assert os.path.isfile(finalpath)

@step(u'When I run "([^"]*)" successfully')
def when_i_run_group1_successfully(step, group1):
	os.system('cd command') 
	os.system('python command.py') 

@step(u'Then I will have the followin result:')
def then_i_will_have_the_followin_result(step): 

	list = []
	a = open('result.txt','r')
	read = a.readlines() 
	for i in range(len(read)): 
		list.append(read[i].rstrip('\n'))

	for row in step.hashes:
		b = row['result'] 
		print b
		if str(b) not in list:
		    assert False
