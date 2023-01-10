from datetime import datetime
from unittest.mock import patch

import pytest

from tests.e2e.responses.timeline_messages import testdata

ROUTE_TIMELINE_ALICE = "/timelines/alice/messages"
PUBLISHING_TIME = datetime(2000, 1, 1, 00, 00, 00)




@patch('src.social_network.domain.timeline.PublishingTime')
def test_should_give_us_the_messages_when_we_fetch_the_timeline(mocked_published_time, test_client,
                                                                ):
    mocked_published_time.return_value = PUBLISHING_TIME
    expected_response = {
        "user": "alice",
        "messages": [
            {"message": "Functional programming is cool", "created_at": "2000-01-01T00:00:00"},
        ]
    }

    payload = {
        "message": "Functional programming is cool", "publisher": "alice", "timeline_user": "alice"
    }

    test_client.post(ROUTE_TIMELINE_ALICE, json=payload)
    response = test_client.get(ROUTE_TIMELINE_ALICE)
    assert response.status_code == 200
    assert response.json() == expected_response

@pytest.mark.parametrize(
    "payload,expected_status_code,expected_response",
    testdata,
    ids=[
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
