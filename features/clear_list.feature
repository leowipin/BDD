Feature: Clear the entire to-do list
  As a user, I want to be able to clear my entire to-do list.

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty
