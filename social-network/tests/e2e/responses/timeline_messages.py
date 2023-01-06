RESPONSE_OK = {}
ERROR_RESPONSE_MESSAGE = {
    "detail": [
        {
            "ctx": {"limit_value": 1},
            "loc": ["body", "message"],
            "msg": "ensure this value has at least 1 characters",
            "type": "value_error.any_str.min_length",
        }
    ]
}
ERROR_RESPONSE_PUBLISHER = {
    "detail": [
        {
            "ctx": {"limit_value": 1},
            "loc": ["body", "publisher"],
            "msg": "ensure this value has at least 1 characters",
            "type": "value_error.any_str.min_length",
        }
    ]
}
ERROR_RESPONSE_TIMELINE_USER = {
    "detail": [
        {
            "ctx": {"limit_value": 1},
            "loc": ["body", "timeline_user"],
            "msg": "ensure this value has at least 1 characters",
            "type": "value_error.any_str.min_length",
        }
    ]
}

testdata = [
    (
        {
            "message": "Functional programming is cool",
            "publisher": "alice",
            "timeline_user": "alice",
        },
        201,
        RESPONSE_OK,
    ),
    (
        {"message": "", "publisher": "alice", "timeline_user": "alice"},
        422,
        ERROR_RESPONSE_MESSAGE,
    ),
    (
        {"message": "dsdsdasdasdasdasd", "publisher": "", "timeline_user": "alice"},
        422,
        ERROR_RESPONSE_PUBLISHER,
    ),
    (
        {"message": "dsdsdasdasdasdasd", "publisher": "alice", "timeline_user": ""},
        422,
        ERROR_RESPONSE_TIMELINE_USER,
    ),
]
