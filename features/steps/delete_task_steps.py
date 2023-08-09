from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_impl(context):
    context.to_do_list = ToDoList()
    for row in context.table:
        context.to_do_list.add_task(row['Task'])

@when('the user deletes the task "{task}"')
def step_impl(context, task):
    context.to_do_list.delete_task(task)

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    assert task not in context.to_do_list.list_tasks()
