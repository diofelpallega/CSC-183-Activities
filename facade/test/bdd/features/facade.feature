Feature: Using facade I want to get the forecast in London
	 
	 As a user I want to get the weather forecast 
	 of a location

	 Scenario Outline: Get weather forecast 
	 Given I have the following:
	     | city   | country | 	  
	     | London |    UK   |  
	 When I run the program
	 Then I get the the following:
	     | city   | country | forecast  |	  
	     | London |    UK   |   5.358   |
 