Feature: Observer to notify the time in eu or usa time 

		 As a User I want to know the date and time 
		 in eu or usa format

		 Scenario: Get time from Usa and Eu observer
		 Given I have an "observer.py" file 
		 When I run "observer.py" successfully
		 Then I see the results
