@smoke
Feature: Login functionality for OrangeHRM

  Scenario Outline: Login with different credentials
    Given the user is on the OrangeHRM login page
    When the user enters username "<username>" and password "<password>"
    Then login should "<result>"

    Examples:
      | username          | password        | result    |
      | Admin             | admin123        | success   |
      | Admin             | wrongpass       | failure   |
      | wronguser         | admin123        | failure   |
      | user123           | pass123         | failure   |
      | admin123          | Admin           | failure   |