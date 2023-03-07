from pytest_archon import archrule


def test_rule_basic():
    (
        archrule("archi rule name", comment="some comment")
        .match("pytest_archon.col*")
        .exclude("pytest_archon.colgate")
        .should_not_import("pytest_archon.import_finder")
        .should_import("pytest_archon.core*")
        .check("pytest_archon")
    )
