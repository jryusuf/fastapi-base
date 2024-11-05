import pytest
from app.models.source import Source


def test_Given_a_new_source_When_creating_source_Then_source_attributes_are_set_correctly():
    # Given
    source_url = "https://example.com/research"
    source_name = "Example Research Paper"

    # When
    source = Source(url=source_url, name=source_name)

    # Then
    assert source.url == source_url
    assert source.name == source_name


def test_Given_multiple_sources_When_creating_sources_Then_each_source_has_unique_attributes():
    # Given
    source1_url = "https://academic.org/paper1"
    source1_name = "First Academic Paper"
    source2_url = "https://academic.org/paper2"
    source2_name = "Second Academic Paper"

    # When
    source1 = Source(url=source1_url, name=source1_name)
    source2 = Source(url=source2_url, name=source2_name)

    # Then
    assert source1.url != source2.url
    assert source1.name != source2.name
