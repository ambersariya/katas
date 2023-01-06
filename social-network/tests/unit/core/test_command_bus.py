import pymessagebus.api
import pytest
from pymessagebus.api import CommandHandlerNotFound


def test_should_dispatch_a_given_command_to_right_handler(
    command_bus, fake_command, pycommandbus
):
    command_bus.dispatch(command=fake_command)
    pycommandbus.handle.assert_called_once_with(fake_command)


def test_should_raise_exception_when_handler_for_command_is_not_found(
    pycommandbus, command_bus, fake_command
):
    pycommandbus.handle.side_effect = pymessagebus.api.CommandHandlerNotFound()

    with pytest.raises(CommandHandlerNotFound):
        command_bus.dispatch(command=fake_command)
