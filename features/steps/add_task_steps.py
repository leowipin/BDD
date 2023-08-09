from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.to_do_list = ToDoList()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.to_do_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert task in context.to_do_list.list_tasks()
