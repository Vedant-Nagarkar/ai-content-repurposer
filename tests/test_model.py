from unittest.mock import MagicMock, patch
from src.model import generate


def test_generate_returns_string():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "This is a mocked response."

    with patch("src.model.client.chat.completions.create", return_value=mock_response):
        result = generate("Test prompt")
        assert isinstance(result, str)
        assert len(result) > 0


def test_generate_strips_whitespace():
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "   Mocked output with spaces.   "

    with patch("src.model.client.chat.completions.create", return_value=mock_response):
        result = generate("Test prompt")
        assert result == "Mocked output with spaces."