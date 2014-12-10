Feature: A proxy to create an object to count references 
         to the cached object that sorts 10 million digits

         As a user, I want to sort randomized digits in a list

         Scenario: Get reference counts
         Given I have "proxy.py" on my directory  
         When I run the "proxy.py" successful
         Then I will have this result:
         	|        Result                                                               |
            | Created new objects 														  |
		    | Count of references =  1 													  |
            | Using cached objects 														  |
            | Count of references =  2 													  |
            | Using cached objects 														  |
            | Count of references =  3     												  |
            | Called sort method with args:												  |
            | [('self', <__main__.Proxy object at 0x7ffc84c8e310>), ('reverse', True)]    |
            | Deleting proxy2 															  |
            | Deleted object. Count of objects =  2                  					  |
            | The other objects are deleted upon program termination  					  |
            | Deleted object. Count of objects =  1 									  |
            | Number of reference_count is 0. Deleting cached object... 				  |
            | Deleted object. Count of objects =  0 				                      |
 
         

