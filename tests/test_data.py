import pytest
from src.data import validate_and_clean


def test_empty_input_raises():
    with pytest.raises(ValueError):
        validate_and_clean("")


def test_whitespace_only_raises():
    with pytest.raises(ValueError):
        validate_and_clean("   ")


def test_short_input_raises():
    with pytest.raises(ValueError):
        validate_and_clean("This is too short.")


def test_valid_input_returns_cleaned():
    text = " " + "word " * 35
    result = validate_and_clean(text)
    assert result == text.strip()
    assert len(result.split()) >= 30