Feature: List all tasks in the to-do list
  As a user, I want to be able to see all the tasks in my to-do list.

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """
