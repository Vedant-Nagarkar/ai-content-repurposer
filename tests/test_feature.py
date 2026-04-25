import pytest
from src.features import build_prompt

SAMPLE_TEXT = "word " * 50


def test_linkedin_prompt_returns_string():
    result = build_prompt(SAMPLE_TEXT, "LinkedIn Post")
    assert isinstance(result, str)
    assert len(result) > 0


def test_twitter_prompt_returns_string():
    result = build_prompt(SAMPLE_TEXT, "Twitter Thread")
    assert isinstance(result, str)
    assert len(result) > 0


def test_executive_prompt_returns_string():
    result = build_prompt(SAMPLE_TEXT, "Executive Summary")
    assert isinstance(result, str)
    assert len(result) > 0


def test_invalid_format_raises():
    with pytest.raises(ValueError):
        build_prompt(SAMPLE_TEXT, "Invalid Format")