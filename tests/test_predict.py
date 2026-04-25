import pytest
from unittest.mock import patch
from src.predict import run_pipeline

VALID_TEXT = "word " * 50


def test_pipeline_returns_string():
    with patch("src.predict.generate", return_value="This is a mocked generated output with enough words to pass evaluation checks easily without any issues at all today."):
        result = run_pipeline(VALID_TEXT, "LinkedIn Post")
        assert isinstance(result, str)
        assert len(result) > 0


def test_pipeline_invalid_format_raises():
    with patch("src.predict.generate", return_value="Mocked output"):
        with pytest.raises(ValueError):
            run_pipeline(VALID_TEXT, "Invalid Format")


def test_pipeline_empty_input_raises():
    with pytest.raises(ValueError):
        run_pipeline("", "LinkedIn Post")