import unittest
from unittest.mock import patch
from ai_model import generate_text

class TestAIModel(unittest.TestCase):
    """Test cases for AI model functionality"""

    @patch('ai_model.client.chat.completions.create')
    def test_generate_text_success(self, mock_create):
        # Mock successful API response
        mock_create.return_value.choices[0].message.content = "Test summary"
        
        result = generate_text("Test prompt")
        self.assertEqual(result, "Test summary")
        mock_create.assert_called_once()

    @patch('ai_model.client.chat.completions.create')
    def test_generate_text_error(self, mock_create):
        # Mock API error
        mock_create.side_effect = Exception("API Error")
        
        result = generate_text("Test prompt")
        self.assertTrue(result.startswith("An error occurred")) 