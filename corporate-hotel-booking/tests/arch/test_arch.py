from pytest_archon import archrule


def test_rule_hotel_should_not_import_from_any_other_package():
    (
        archrule("hotel package should not import from other packages", comment="some comment")
        .match("src.hotel*")
        .should_not_import("src.company*")
        .should_not_import("src.booking*")
        .check("src")
    )


def test_rule_company_should_not_import_from_any_other_package():
    (
        archrule("company package should not import from other packages", comment="some comment")
        .match("src.company*")
        .should_not_import("src.hotel*")
        .should_not_import("src.booking*")
        .check("src")
    )


def test_rule_booking_should_not_import_from_any_other_package():
    (
        archrule("company package should not import from other packages", comment="some comment")
        .match("src.booking*")
        .should_not_import("src.hotel*")
        .should_not_import("src.company*")
        .check("src")
    )
