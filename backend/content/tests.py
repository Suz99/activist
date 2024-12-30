"""
Testing for the content app.
"""

# mypy: ignore-errors
from .factories import ResourceFactory, TaskFactory, TopicFactory

import pytest

pytestmark = pytest.mark.django_db


def test_str_methods() -> None:
    resource = ResourceFactory.build()
    task = TaskFactory.build()
    topics = TopicFactory.build()

    assert str(resource) == resource.name
    assert str(task) == task.name
    assert str(topics) == topics.name
