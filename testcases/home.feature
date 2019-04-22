Feature: to verify create account functionality of facebook

  Background:
    Given user has launched 'chrome' browser and 'http://fb.com' app
    Then  verify page 'title' is 'facebook - log in sign up'

  Scenario: create account with invalid mobile number
    And pass first name as 'prashant'
    And pass last name as 'khande'
    And pass mobile number or email as '8421835355'
    And pass password as 'khande123'
    And select date as '14'
    And select month as 'sept'
    And select year as '1996'
    And selecct gender as 'male'
    Then click on sign up button



  Scenario: create account by selecting female radio button
    Then pass first name as 'prashant'

