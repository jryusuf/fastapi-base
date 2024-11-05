import pytest
import uuid
from app.models.project import Project


def test_Given_a_project_When_adding_sources_Then_sources_list_is_updated_correctly():
    # Given
    project = Project(name="Data Collection Project")

    # When
    source1 = "Academic Paper"
    source2 = "Research Report"
    project.add_source(source1)
    project.add_source(source2)

    # Then
    assert len(project.sources) == 2
    assert source1 in project.sources
    assert source2 in project.sources


def test_Given_a_new_project_When_no_sources_added_Then_sources_list_is_empty():
    # Given
    project_name = "Empty Project"

    # When
    project = Project(name=project_name)

    # Then
    assert len(project.sources) == 0
    assert project.sources == []


def test_Given_a_new_project_When_creating_project_Then_project_has_a_unique_uuid():
    # Given
    project_name = "UUID Project"

    # When
    project = Project(name=project_name)

    # Then
    assert hasattr(project, 'id')
    assert isinstance(project.id, uuid.UUID)

    # Create another project to ensure UUIDs are unique
    project2 = Project(name="Another UUID Project")
    assert project.id != project2.id


def test_Given_a_project_When_updating_status_Then_only_specific_statuses_are_allowed():
    # Given
    project = Project(name="Status Test Project")
    valid_statuses = ['RUNNING', 'STOPPED', 'PAUSED']
    invalid_statuses = ['In Progress', 'Completed', 'Draft', '']

    # When & Then
    for status in valid_statuses:
        project.update_status(status)  # Should not raise an exception

    # Check that invalid statuses raise an exception
    for status in invalid_statuses:
        with pytest.raises(ValueError, match="Invalid project status"):
            project.update_status(status)


def test_Given_a_new_project_When_creating_project_Then_default_status_is_stopped():
    # Given & When
    project = Project(name="Default Status Project")

    # Then
    assert project.status == 'STOPPED'

    # When
    project.update_status('RUNNING')

    # Then
    assert project.status == 'RUNNING'

    # When
    project.update_status('PAUSED')

    # Then
    assert project.status == 'PAUSED'
