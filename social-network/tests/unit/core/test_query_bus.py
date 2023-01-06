import pytest

from src.core.query import QueryHandlerNotFound


def test_should_dispatch_a_given_query_to_right_handler(
    query_bus, pyquerybus, fake_query
):
    query_bus.dispatch(query=fake_query)
    pyquerybus.handle.assert_called_once_with(fake_query)


def test_should_raise_exception_when_handler_for_query_is_not_found(
    fake_query, query_bus, pyquerybus
):
    pyquerybus.has_handler_for.return_value = False
    with pytest.raises(QueryHandlerNotFound):
        query_bus.dispatch(query=fake_query)
