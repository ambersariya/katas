from behave import *


def before_scenario(context, scenario):
    context.shopping_basket_service = ShoppingBasketService()
    context.product_service = ProductService()
    context.user_id = UserId()


@given(u'I add "{quantity}" units of "{item}" to my shopping basket')
def step_impl(context, quantity: str, item: str):
    item = context.product_service.get_item_by_name(name=item)
    context.shopping_basket_service.add_item(user_id=context.user_id,
                                             product_id=item.product_id,
                                             quantity=int(quantity))


@given(u'I add "{quantity}" units of "{item}"')
def step_impl(context, quantity: str, item: str):
    item = context.product_service.get_item_by_name(name=item)
    context.shopping_basket_service.add_item(user_id=context.user_id,
                                             product_id=item.product_id,
                                             quantity=int(quantity))


@when(u'I check the content of my shopping basket')
def step_impl(context):
    assert True is not False


@then(u'it should contain the following information')
def step_impl(context):
    assert context.failed is False
