import logging

import pytest
from utils.APIs import API

@pytest.fixture(scope="module")
def apis():
    return API()


def test_get_api(apis):
    response = apis.get("api/v1/Activities")
    assert len(response.json()) > 0
    data = response.json()
    print(data)
    logging.info("Status code: %s", response.status_code)
    assert response.status_code == 200


