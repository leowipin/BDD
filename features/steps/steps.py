from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.to_do_list = ToDoList()

@given('the to-do list contains tasks')
def step_impl(context):
    context.to_do_list = ToDoList()
    for row in context.table:
        context.to_do_list.add_task(row['Task'])

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.to_do_list.add_task(task)

@when('the user clears the to-do list')
def step_impl(context):
    context.to_do_list.clear_list()

@when('the user deletes the task "{task}"')
def step_impl(context, task):
    context.to_do_list.delete_task(task)

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = context.to_do_list.list_tasks()

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.to_do_list.mark_task_complete(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert task in context.to_do_list.list_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.to_do_list.tasks) == 0

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    assert task not in context.to_do_list.list_tasks()

@then('the output should contain')
def step_impl(context):
    expected_output = context.text.strip().split('\n')[1:]
    expected_output = [task.strip('-\r ') for task in expected_output]
    print(f'expected_output: {expected_output}')
    print(f'context.listed_tasks: {context.listed_tasks}')

    assert expected_output == context.listed_tasks

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.to_do_list.tasks:
        if t.description == task:
            assert t.status == 'Complete'
