Feature: Observer to notify the time in eu or usa time 

		 As a User I want to know the date and time 
		 in eu or usa format

		 Scenario: Get time from Usa and Eu observer
		 Given I have an "observer.py" file 
		 When I run "observer.py" successfully
		 Then I see results:
		  |             Results 		|       Time             | 
		  |     Adding usa_time_observer        |	                 |
		  |	Observer usa_time_observer says: |2014-12-11 06:32:47PM  |
		  |	Adding eu_time_observer         |                        |
		  |	Observer usa_time_observer says:| 2014-12-11 06:32:47PM  |
		  |	Observer eu_time_observer says: | 2014-12-11 18:31:47    |
		  |	removing usa_time_observer      |                        |
		  |	Observer eu_time_observer says: |  2014-12-11 18:31:47   |

 
