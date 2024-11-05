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


def test_Given_a_user_When_adding_projects_Then_only_project_objects_are_allowed():
    # Given
    user = User(username="project_validation_user",
                email="validation@example.com", password="secret")
    valid_project = Project(name="Valid Project")

    # When & Then
    user.add_project(valid_project)
    assert len(user.projects) == 1
    assert user.projects[0] == valid_project

    # Try adding invalid projects
    invalid_projects = [
        "Not a Project object",
        123,
        None,
        {"name": "Dict Project"}
    ]

    # Check that adding non-Project objects raises an exception
    for invalid_project in invalid_projects:
        with pytest.raises(TypeError, match="Only Project objects can be added to a user"):
            user.add_project(invalid_project)
