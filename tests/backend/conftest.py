from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    # Arrange
    test_client = TestClient(app)

    # Act
    yield test_client

    # Assert
    # No explicit assertions for fixture teardown.


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange
    original_activities = deepcopy(activities)

    # Act
    yield

    # Assert
    activities.clear()
    activities.update(deepcopy(original_activities))