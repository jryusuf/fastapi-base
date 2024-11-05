import pytest
import uuid
from app.models.user import User
from app.models.project import Project
from app.models.source import Source, InvalidURLError


def test_Given_a_user_When_creating_project_and_adding_sources_Then_project_is_correctly_configured():
    # Given
    user = User(username="research_user",
                email="research@example.com", password="secure")

    # When
    project = Project(name="Research Data Collection")

    # Add valid sources to the project
    source1 = Source(url="https://academic.org/paper1",
                     name="First Research Paper")
    source2 = Source(url="https://academic.org/paper2",
                     name="Second Research Paper")

    project.add_source(source1)
    project.add_source(source2)

    # Add project to user
    user.add_project(project)

    # Then
    assert len(project.sources) == 2
    assert source1 in project.sources
    assert source2 in project.sources

    assert len(user.projects) == 1
    assert project in user.projects
    assert project.status == 'STOPPED'


def test_Given_a_user_When_creating_multiple_projects_with_different_statuses_Then_projects_are_managed_correctly():
    # Given
    user = User(username="multi_project_user",
                email="multi@example.com", password="complex")

    # When
    project1 = Project(name="Active Research")
    project2 = Project(name="Paused Development")

    project1.update_status('RUNNING')
    project2.update_status('PAUSED')

    user.add_project(project1)
    user.add_project(project2)

    # Then
    assert len(user.projects) == 2
    user_project1 = user.projects[0]
    user_project2 = user.projects[1]
    assert user_project1.status == 'RUNNING'
    assert user_project2.status == 'PAUSED'


def test_Given_a_user_When_adding_project_with_multiple_sources_Then_sources_are_validated():
    # Given
    user = User(username="source_validation_user",
                email="validation@example.com", password="strict")
    project = Project(name="Comprehensive Research")

    # When
    valid_sources = [
        Source(url="https://research.org/paper1", name="First Paper"),
        Source(url="https://research.org/paper2", name="Second Paper")
    ]

    for source in valid_sources:
        project.add_source(source)

    user.add_project(project)
    user_project = user.projects[0]

    # Then
    assert len(user_project.sources) == 2
    assert len(user.projects) == 1


def test_Given_a_user_When_attempting_to_add_invalid_sources_Then_exceptions_are_raised():
    # Given
    user = User(username="strict_user",
                email="strict@example.com", password="secure")
    project = Project(name="Strict Research")

    # When & Then
    with pytest.raises(InvalidURLError, match="Invalid URL format"):
        Source(url="invalid_url", name="Invalid Source")

    with pytest.raises(TypeError, match="Only Source objects can be added to a project"):
        project.add_source("Not a source")

    with pytest.raises(TypeError, match="Only Project objects can be added to a user"):
        user.add_project("Not a project")


def test_Given_a_user_When_creating_projects_with_sources_Then_uuids_are_unique():
    # Given
    user = User(username="uuid_user",
                email="uuid@example.com", password="unique")

    # When
    project1 = Project(name="First Project")
    project2 = Project(name="Second Project")

    source1 = Source(url="https://example1.com", name="Source 1")
    source2 = Source(url="https://example2.com", name="Source 2")

    # Add sources to projects
    project1.add_source(source1)
    project2.add_source(source2)

    # Add projects to user
    user.add_project(project1)
    user.add_project(project2)

    # Then
    assert project1.id != project2.id
    assert source1.id != source2.id

    # Verify no duplicate UUIDs in projects and sources
    project_ids = [project.id for project in user.projects]
    source_ids = [
        source.id for project in user.projects for source in project.sources]

    assert len(set(project_ids)) == len(project_ids)
    assert len(set(source_ids)) == len(source_ids)
