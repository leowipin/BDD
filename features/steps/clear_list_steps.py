from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_impl(context):
    context.to_do_list = ToDoList()
    for row in context.table:
        context.to_do_list.add_task(row['Task'])

@when('the user clears the to-do list')
def step_impl(context):
    context.to_do_list.clear_list()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.to_do_list.tasks) == 0
