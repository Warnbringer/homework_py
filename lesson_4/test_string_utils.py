import pytest
from StringUtils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


@pytest.mark.parametrize("input_str, expected_output", [
    ("skypro", "Skypro"),
    ("SKYPRO", "Skypro"),
    ("hi hi", "Hi hi"),
])
def test_capitalize_pos(string_utils, input_str, expected_output):
    assert string_utils.capitilize(input_str) == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    (" ", " "),
    ("", ""),
    ("123", "123"),
])
def test_capitalize_neg(string_utils, input_str, expected_output):
    assert string_utils.capitilize(input_str) == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    ("   skypro   ", "skypro"),
    ("skypro", "skypro"),
    ("   ", ""),
])
def test_trim_pos(string_utils, input_str, expected_output):
    assert string_utils.trim(input_str) == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    ("skypro", "skypro"),
    ("", ""),
])
def test_trim_neg(string_utils, input_str, expected_output):
    assert string_utils.trim(input_str) == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    ("a,b,c", ["a", "b", "c"]),
    ("a b c", ["a", "b", "c"]),
    ("", []),
])
def test_to_list_pos(string_utils, input_str, expected_output):
    assert string_utils.to_list(input_str) == expected_output


@pytest.mark.parametrize("input_str, delimiter, expected_output", [
    ("a,b,c", ";", ["a,b,c"]),
])
def test_to_list_neg(string_utils, input_str, delimiter, expected_output):
    assert string_utils.to_list(input_str, delimiter) == expected_output


@pytest.mark.parametrize("input_str, char, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
])
def test_contains(string_utils, input_str, char, expected_output):
    assert string_utils.contains(input_str, char) == expected_output


@pytest.mark.parametrize("input_str, char, expected_output", [
    ("SkyPro", "r", "SkyPo"),
    ("SkyPro", "Pro", "Sky"),
    ("", "x", ""),
])
def test_delete_symbol(string_utils, input_str, char, expected_output):
    assert string_utils.delete_symbol(input_str, char) == expected_output


@pytest.mark.parametrize("input_str, char, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "p", False),
])
def test_starts_with(string_utils, input_str, char, expected_output):
    assert string_utils.starts_with(input_str, char) == expected_output


@pytest.mark.parametrize("input_str, char, expected_output", [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "o", False),
])
def test_end_with(string_utils, input_str, char, expected_output):
    assert string_utils.end_with(input_str, char) == expected_output


@pytest.mark.parametrize("input_str, expected_output", [
    ("", True),
    ("  ", True),
    ("SkyPro", False),
])
def test_is_empty(string_utils, input_str, expected_output):
    assert string_utils.is_empty(input_str) == expected_output


@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 2, 3, 4], "1, 2, 3, 4"),
    (["Sky", "Pro"], "Sky, Pro"),
    (["Sky", "Pro"], "Sky-Pro"),
])
def test_list_to_string(string_utils, input_list, expected_output):
    assert string_utils.list_to_string(input_list) == expected_output
