Feature: A command that implements unix commands ls,rm,touch

		 As a User I want to get list,remove and touch files
		 in my present directory

		 Scenario: get files, touch, remove file
		 Give I have a file named "command.py"
		 When I run "command.py" successfully
		 Then I will have the followin result:
		     |   result     						|
		     |Creating file...						|
		     |Content of dir:  command.py			|
		     |Content of dir:  command.py test_file |
		     |File created.							|
		     |Deleting file...						|
		     |Content of dir:  command.py test_file |
		     |Content of dir:  .test_file command.py|
		     |File deleted.							|
 