from behave import *


@given(u'I add "{quantity}" units of "{item}" to my shopping basket')
def step_impl(context, quantity: str, item: str):
    pass


@given(u'I add "{quantity}" units of "{item}"')
def step_impl(context, quantity: str, item: str):
    pass


@when(u'I check the content of my shopping basket')
def step_impl(context):
    assert True is not False


@then(u'it should contain the following information')
def step_impl(context):
    assert context.failed is False
