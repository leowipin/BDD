from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_impl(context):
    context.to_do_list = ToDoList()
    for row in context.table:
        context.to_do_list.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = context.to_do_list.list_tasks()

@then('the output should contain:')
def step_impl(context):
    expected_output = context.text.strip().split('\n')[1:]
    expected_output = [task.strip('- ') for task in expected_output]
    assert expected_output == context.listed_tasks
