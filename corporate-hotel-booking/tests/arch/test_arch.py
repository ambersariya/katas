from pytest_archon import archrule


def test_rule_hotel_should_not_import_from_any_other_package():
    (
        archrule("hotel package should not import for other packages", comment="some comment")
        .match("src.hotel*")
        .should_not_import("src.company*")
        .check("src")
    )
