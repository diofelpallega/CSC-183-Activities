Feature: Cd Rental web application to Check In and Out
	     and update customer accounts
	 
	 	 As a clerk I want to be able to checkout customer
	 	 
	 	 Scenario: checkout a cd
	 	 Given I have the following cds:
	     |cd_id|    title    |isrented|rentedBy|
	     |00-01|   3 Idiots  | false  |  none  |
	     |00-02|  Life of Pi | false  |  none  |
	     |00-03| One Piece 1 | false  |  none  |  
	 	 And I have the following listed customers:
  		 |customer_id|  name  |  rented  |  rentedArray  |
  		 |    002    |  jack  |     0    |      []		 | 
  		 Then I visit the homepage to checkout
	 	 When I input customer id "0001" and cd id "00-01"
	 	 Then I see output "checkout successful" 
 