from pytest_archon import archrule


def test_rule_core_should_not_import_any_other_packages():
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

# def test_rule_core_should_not_import_any_other_packages():
#     archrule("archi rule name", comment="some comment") \
#         .match("shopping_basket.core*") \
#         .should_not_import("shopping_basket.api") \
#         .should_not_import("shopping_basket.basket") \
#         .should_not_import("shopping_basket.discount") \
#         .should_not_import("shopping_basket.order") \
#         .should_not_import("shopping_basket.payment") \
#         .should_not_import("shopping_basket.product") \
#         .should_not_import("shopping_basket.purchase") \
#         .should_not_import("shopping_basket.stock") \
#         .check("shopping_basket.core")
