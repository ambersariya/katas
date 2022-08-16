from behave import *


def before_all(context):
    context.shopping_basket_service = ShoppingBasketService()
    context.product_service = ProductService()
    context.user_id = UserId()


@given('I add "{quantity}" units of "{item_name}" to my shopping basket')
def step_impl(context, quantity: str, item_name: str):
    item = context.product_service.get_item_by_name(name=item_name)
    context.shopping_basket_service.add_item(
        user_id=context.user_id, product_id=item.product_id, quantity=int(quantity)
    )


@given('I add "{quantity}" units of "{item_name}"')
def step_impl(context, quantity: str, item_name: str):
    item = context.product_service.get_item_by_name(name=item_name)
    context.shopping_basket_service.add_item(
        user_id=context.user_id, product_id=item.product_id, quantity=int(quantity)
    )


@when("I check the content of my shopping basket")
def step_impl(context):
    context.basket = context.shopping_basket_service.basket_for(context.user_id)


@then("it should contain the following information")
def step_impl(context, basket_printout: str):
    assert str(context.basket) == basket_printout
