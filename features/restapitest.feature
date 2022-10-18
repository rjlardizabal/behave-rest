Feature: Rest API Example Test

  Background: Setup environment
    Given I set base URL to "http://dummy.restapiexample.com/api/v1"
    And I set "Accept" header to "application/json"
    And I set "User-Agent" header to "context.user_agent"


  @search @restapiexample
  Scenario: Get Employee
    When I make a GET request to "employee/1"
    Then the response status code should equal 200
    And the response header "Response" should equal "200"
    Then JSON at path ".data.id" should equal 1
    Then JSON at path ".data.employee_name" should equal "Tiger Nixon"
    Then JSON at path ".data.employee_salary" should equal 320800
    Then JSON at path ".data.employee_age" should equal 61
    Then JSON at path ".data.profile_image" should equal ""
    And the response parameter "message" should equal "Successfully! Record has been fetched."
    And the response structure should equal "responseData"

