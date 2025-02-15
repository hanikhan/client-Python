"""This module contains common Pytest fixtures and hooks for unit tests."""

from six.moves import mock

# noinspection PyPackageRequirements
from pytest import fixture

from reportportal_client.client import RPClient


@fixture()
def response():
    """Cook up a mock for the Response with specific arguments."""
    def inner(ret_code, ret_value):
        """Set up response with the given parameters.

        :param ret_code:  Return code for the response
        :param ret_value: Return value for the response
        :return:          Mocked Responce object with the given parameters
        """
        with mock.patch('requests.Response') as resp:
            resp.status_code = ret_code
            resp.json.return_value = ret_value
            return resp
    return inner


@fixture
def rp_client():
    """Prepare instance of the RPClient for testing."""
    client = RPClient('http://endpoint', 'project', 'token')
    client.session = mock.Mock()
    return client
