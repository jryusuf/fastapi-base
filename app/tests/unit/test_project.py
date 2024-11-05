import pytest
from app.models.project import Project


def test_Given_a_new_project_When_creating_project_Then_project_attributes_are_set_correctly():
    # Given
    project_name = "Research Project"

    # When
    project = Project(name=project_name)

    # Then
    assert project.name == project_name
    assert project.sources == []
    assert project.status == 'Not Started'


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


def test_Given_a_project_When_updating_status_Then_project_status_changes_correctly():
    # Given
    project = Project(name="Implementation Project")

    # When
    initial_status = project.status
    project.update_status("In Progress")

    # Then
    assert initial_status == 'Not Started'
    assert project.status == 'In Progress'
