Feature: Delete a task from the to-do list
  As a user, I want to be able to delete a specific task from my to-do list.

  Scenario: Delete a task from the to-do list
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
      | Pay bills |
    When the user deletes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"
