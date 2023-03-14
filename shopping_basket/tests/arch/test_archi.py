from unittest import skip

from pytest_archon import archrule


def test_core_should_not_import_any_other_packages():
    archrule(
        "Core should not import from other domain packages",
        comment="Core is a common package and it can be imported in other packages"
    ) \
        .match("shopping_basket.core*") \
        .should_not_import("shopping_basket.api*") \
        .should_not_import("shopping_basket.basket*") \
        .should_not_import("shopping_basket.discount*") \
        .should_not_import("shopping_basket.order*") \
        .should_not_import("shopping_basket.payment*") \
        .should_not_import("shopping_basket.product*") \
        .should_not_import("shopping_basket.purchase*") \
        .should_not_import("shopping_basket.stock*") \
        .check("shopping_basket.core")


def test_basket_should_not_import_any_other_packages_except_core():
    archrule(
        name="Basket package should not import any other packages except core",
        comment="some comment"
    ).match('shopping_basket.basket*') \
        .may_import('shopping_basket.core*') \
        .may_import('shopping_basket.basket.product') \
        .should_not_import("shopping_basket.api*") \
        .should_not_import("shopping_basket.payment*") \
        .should_not_import("shopping_basket.discount*") \
        .should_not_import("shopping_basket.order*") \
        .should_not_import("shopping_basket.purchase*") \
        .should_not_import("shopping_basket.stock*") \
        .check('shopping_basket.basket')


@skip(reason='need to come back to this')
def test_payment_should_not_import_any_other_packages_except_core():
    archrule(
        name="Payment package should not import any other packages except core",
        comment="some comment"
    ).match('shopping_basket.payment*') \
        .may_import('shopping_basket.core*') \
        .should_not_import("shopping_basket.api*") \
        .should_not_import("shopping_basket.basket*") \
        .should_not_import("shopping_basket.discount*") \
        .should_not_import("shopping_basket.order*") \
        .should_not_import("shopping_basket.product*") \
        .should_not_import("shopping_basket.purchase*") \
        .should_not_import("shopping_basket.stock*") \
        .check('shopping_basket.payment')

def test_product_should_not_import_any_other_packages_except_core():
    archrule(
        name="Product package should not import any other packages except core",
        comment="some comment"
    ).match('shopping_basket.product*') \
        .may_import('shopping_basket.core*') \
        .should_not_import("shopping_basket.api*") \
        .should_not_import("shopping_basket.basket*") \
        .should_not_import("shopping_basket.discount*") \
        .should_not_import("shopping_basket.order*") \
        .should_not_import("shopping_basket.payment*") \
        .should_not_import("shopping_basket.purchase*") \
        .should_not_import("shopping_basket.stock*") \
        .check('shopping_basket.payment')
