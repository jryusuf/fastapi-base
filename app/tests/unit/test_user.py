import pytest
from app.models.user import User
from app.models.project import Project


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


def test_Given_a_user_When_adding_projects_Then_projects_list_is_updated_correctly():
    # Given
    user = User(username="projectuser",
                email="projectuser@example.com", password="secret")

    # When
    project1 = Project(name="Research Project")
    project2 = Project(name="Development Project")
    user.add_project(project1)
    user.add_project(project2)

    # Then
    assert len(user.projects) == 2
    assert project1 in user.projects
    assert project2 in user.projects
