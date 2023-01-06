import pytest

from tests.e2e.responses.timeline_messages import testdata

ROUTE_TIMELINE_ALICE = "/timelines/alice/messages"


@pytest.mark.parametrize(
    "payload,expected_status_code,expected_response",
    testdata,
    ids=[
        "published created 201",
        "message invalid 422",
        "publisher invalid 422",
        "timeline user invalid 422",
    ],
)
def test_should_give_us_response_when_we_post_message_to_personal_timeline(
    payload, expected_status_code, expected_response, test_client
):
    response = test_client.post(ROUTE_TIMELINE_ALICE, json=payload)
    assert response.status_code == expected_status_code
    assert response.json() == expected_response
