import pytest
from app.models.user import User


def test_Given_a_new_user_When_creating_user_Then_user_attributes_are_set_correctly():
    # Given
    username = "testuser"
    email = "testuser@example.com"
    password = "secret_password"

    # When
    user = User(username=username, email=email, password=password)

    # Then
    assert user.username == username
    assert user.email == email
    assert user.id is None
    assert user.password is None  # Ensure password is not directly accessible
