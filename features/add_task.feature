Feature: Add a task to the to-do list
  As a user, I want to be able to add a new task to my to-do list.

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"
