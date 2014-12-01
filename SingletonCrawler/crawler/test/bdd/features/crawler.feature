Feature: Crawler application to get images from websites
     
     As a user I want to be able to get images without opening the source on the web  
     

     Scenario: Get image from site
     Given I input site "http://localhost/site.html" 
     When I get image "http://localhost/a.jpg" from "http://localhost/site.html"
     Then "a.jpg" from "http://localhost/site.html" is in "/home/supersherlock/Desktop/REPOS/CSC-183-Activities/SingletonCrawler/crawler/images/"

     
   
 
