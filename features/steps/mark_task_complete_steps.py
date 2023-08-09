from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list contains tasks:')
def step_impl(context):
    context.to_do_list = ToDoList()
    for row in context.table:
        context.to_do_list.add_task(row['Task'])

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.to_do_list.mark_task_complete(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.to_do_list.tasks:
        if t.description == task:
            assert t.status == 'Complete'
